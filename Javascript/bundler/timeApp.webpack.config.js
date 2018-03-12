module.exports = {
    entry : "./TimeApp/TimeApp.js",
    output : {
        filename:'../../../home/static/home/dist/timeApp.js',
    },
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