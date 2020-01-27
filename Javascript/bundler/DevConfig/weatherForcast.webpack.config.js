const path = require('path');

module.exports = {
    entry : "./WeatherApp/WeatherForcastApp.js",
    output : {
        filename:'../../../home/static/home/dist/WeatherForcastApp.js',
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