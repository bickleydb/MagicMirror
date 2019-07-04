const path = require('path');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    entry : "./StatementApp/StatementApp.js",
    output : {
        filename: '../../../statements/static/statements/JS/StatementApp.js',
    },

    mode : "development",
    optimization: {
        minimizer: [new UglifyJsPlugin()],
    },
    module:  {
        rules: [
            {
                exclude : [
                    path.resolve(__dirname, "/Framework/"),
                    path.resolve(__dirname, "/Common/")
                ]
            }
        ]
    }
};