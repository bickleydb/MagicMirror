module.exports = {
    entry : "./WeatherApp/WeatherApp.js",
    output : {
        filename:'/www/MagicMirror/MagicMirror/home/static/home/dist/WeatherApp.js',
    },
    mode : "development",
    
    module:  {
        rules: [
            {
                exclude : [
                    "/www/MagicMirror/MagicMirror/Framework/*",
                    "/www/MagicMirror/MagicMirror/Common/*",
                ]
            }
        ]
    }
};