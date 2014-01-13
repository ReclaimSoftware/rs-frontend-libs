var fs = require('fs');

module.exports = {
  PUBLIC_DIR: fs.realpathSync(__dirname + "/public")
};
