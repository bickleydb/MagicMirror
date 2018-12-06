module.exports = {
    entry : "./WeatherApp/WeatherApp.js",
    output : {
        filename:'../../../home/static/home/dist/WeatherApp.js',
    },
    mode : "development",
    
    module:  {
        rules: [
            {
                exclude : [
                    "./Framework/*",
                    "./Common/*",
                ]
            }
        ]
    }
};