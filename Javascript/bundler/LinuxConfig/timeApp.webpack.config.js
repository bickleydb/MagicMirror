module.exports = {
    entry : "./TimeApp/TimeApp.js",
    output : {
        filename:'/www/MagicMirror/MagicMirror/home/static/home/dist/timeApp.js',
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