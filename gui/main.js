const { app, BrowserWindow } = require('electron');
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
  win.loadFile('index.html');
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

let body = document.getElementsByTagName('body');
console.log(body);