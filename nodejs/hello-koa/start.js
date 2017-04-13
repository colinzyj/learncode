var register = require('babel-core/register');

register({
    presets: ['stage-3']
});
//console.log('111');
require('./app.js');
