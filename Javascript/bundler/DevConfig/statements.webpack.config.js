const path = require('path');

module.exports = {
    entry : "./StatementApp/StatementApp.js",
    output : {
        filename: '../../../statements/static/statements/JS/StatementApp.js',
    },

    mode : "development",
    
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