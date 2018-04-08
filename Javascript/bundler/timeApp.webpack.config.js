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
                    "./Framework/*",
                    "./Common/*",
                ]
            }
        ]
    }
};