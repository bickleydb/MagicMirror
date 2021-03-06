const path = require('path');

module.exports = {
    entry : "./TimeApp/TimeApp.js",
    output : {
        filename:'../../../home/static/home/dist/timeApp.js',
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