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
                    "./Framework/*",
                    "./Common/*",
                    "./Common/EventManager.js"
                ]
            }
        ]
    }
};