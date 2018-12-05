const path=require('Path')

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
                    path.resolve(__dirname, "Framework/*"),
                    path.resolve(__dirname, "Common/*"),
                ]
            }
        ]
    }
};