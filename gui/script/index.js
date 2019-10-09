const fs = require('fs');

let configs = {};

// Read configurations and push to configs
fs.readdirSync('../config/').forEach(dir => {
  if (dir != '__pycache__' && dir != 'Configurator.py') {
    let raw = fs.readFileSync('../config/' + dir + '/' + dir + '.json');
    configs[dir] = (JSON.parse(raw));
  }
});
