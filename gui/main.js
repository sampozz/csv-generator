const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const url = require('url');
const path = require('path');
const fs = require('fs');

let win;
let configs = {};

// Read configurations and push to configs
fs.readdirSync('../config/').forEach(dir => {
  if (dir != '__pycache__' && dir != 'Configurator.py') {
    let raw = fs.readFileSync('../config/' + dir + '/' + dir + '.json');
    configs[dir] = (JSON.parse(raw));
  }
});
// Write configs to configs.json file
fs.writeFile(path.join(__dirname, 'assets/configs.json'), JSON.stringify(configs), (err) => {
  if (err) {
    console.log(err);
  }
}); 

// Configure window
app.on('ready', () => {
  win = new BrowserWindow({
    minHeight: 600,
    minWidth: 800,
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });
  win.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file',
    slashes: true,
  }));
  win.on('closed', () => {
    win = null;
  });
});
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
app.on('activate', () => {
  if (win === null) {
    createWindow();
  }
});
