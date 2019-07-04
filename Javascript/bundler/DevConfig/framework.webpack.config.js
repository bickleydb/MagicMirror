const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    entry : "./Framework/Window.js",
    output : {
        filename:'../../../home/static/home/dist/magicmirror.js',
    },
    optimization: {
        minimizer: [new UglifyJsPlugin()],
    },
    devtool: 'eval-source-map',
    mode : "development", 
};