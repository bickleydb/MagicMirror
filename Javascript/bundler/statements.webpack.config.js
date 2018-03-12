module.exports = {
    entry : "./StatementApp/StatementApp.js",
    output : {
        filename:'../../statements/static/statements/JS/StatementApp.js',
    },
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