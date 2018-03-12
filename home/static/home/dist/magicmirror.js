!function(e) {
    var t = {};
    function s(i) {
        if (t[i])
            return t[i].exports;
        var n = t[i] = {
            i: i,
            l: !1,
            exports: {}
        };
        return e[i].call(n.exports, n, n.exports, s),
        n.l = !0,
        n.exports
    }
    s.m = e,
    s.c = t,
    s.d = function(e, t, i) {
        s.o(e, t) || Object.defineProperty(e, t, {
            configurable: !1,
            enumerable: !0,
            get: i
        })
    }
    ,
    s.r = function(e) {
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    s.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return s.d(t, "a", t),
        t
    }
    ,
    s.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    s.p = "",
    s(s.s = 3)
}([function(e, t, s) {
    var i;
    void 0 === (i = function(e, t) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        });
        t.AppStatus = class {
            constructor(e) {
                this.app = e,
                this.hasBeenLoaded = !1,
                this.isWaitingQuery = !1,
                this.isWaitingOnInit = !1
            }
            get App() {
                return this.app
            }
            get HasBeenLoaded() {
                return this.hasBeenLoaded
            }
            get IsWaitingQuery() {
                return this.isWaitingQuery
            }
            get IsWaitingOnInit() {
                return this.isWaitingOnInit
            }
            set IsWaitingOnInit(e) {
                this.isWaitingOnInit = e
            }
            set App(e) {
                this.app = e
            }
            set HasBeenLoaded(e) {
                this.hasBeenLoaded = e
            }
            set IsWaitingQuery(e) {
                this.IsWaitingQuery = e
            }
        }
    }
    .apply(t, [s, t])) || (e.exports = i)
}
, function(e, t, s) {
    var i;
    void 0 === (i = function(e, t) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        });
        t.KeyValueDictionary = class {
            constructor() {
                this.backing = {}
            }
            GetValue(e) {
                if (this.backing[e])
                    return this.backing[e]
            }
            Add(e, t) {
                this.backing[e] && delete this.backing[e],
                this.backing[e] = t
            }
        }
    }
    .apply(t, [s, t])) || (e.exports = i)
}
, function(e, t, s) {
    var i, n;
    i = [s, t, s(1)],
    void 0 === (n = function(e, t, s) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        });
        class i {
            constructor(e) {
                this.owningAppKey = "",
                this.url = e,
                this.queryId = i.idNum,
                this.params = new s.KeyValueDictionary,
                this.returnVals = new s.KeyValueDictionary
            }
            static BuildQuery(e, ...t) {
                let s = new i(e);
                return s.setupParameters(t),
                s
            }
            static SetParamVals(e, ...t) {
                t.forEach(t=>{
                    e.params.Add(t.key, t.value)
                }
                )
            }
            static SetResponseVals(e, ...t) {
                t.forEach(t=>{
                    for (let s in t)
                        e.returnVals.Add(s, t[s])
                }
                )
            }
            GetResults() {}
            setupParameters(e) {
                e.forEach(e=>{
                    this.params.Add(e.key, e.value)
                }
                )
            }
            static updateIdNum() {
                i.idNum++
            }
            get URL() {
                return this.url
            }
            getParams() {
                return this.params
            }
            getOwningAppKey() {
                return this.owningAppKey
            }
            setOwningAppKey(e) {
                this.owningAppKey = e
            }
            getResultVals() {
                return this.returnVals
            }
        }
        i.idNum = 0,
        t.QueryDefinition = i
    }
    .apply(t, i)) || (e.exports = n)
}
, function(e, t, s) {
    var i, n;
    i = [s, t, s(2), s(0)],
    void 0 === (n = function(e, t, s, i) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        });
        window.MagicMirror = new class {
            constructor() {
                this.requestTimer = -1,
                this.mainLoopId = -1,
                this.START_URL = "http://127.0.0.1:8000/startup/",
                this.APP_LIST_URL = "http://127.0.0.1:8000/loadApplications",
                this.APP_LOAD_URL = "http://127.0.0.1:8000/loadApp/",
                this.baseHTMLElement = document.body,
                this.requests = [],
                this.registeredApps = {},
                this.loadApplicationList(),
                this.attachEventHandlers()
            }
            addApplication(e) {
                const t = e.getName();
                if (this.registeredApps[t] = new i.AppStatus(e),
                e.clientOnly())
                    return void e.onInitialRender(this.createAppHTML());
                const s = e.getUIQuery();
                $.ajax(s.URL, {
                    success: t=>{
                        const s = this.createAppHTML();
                        $(s).append(t),
                        e.onInitialRender(s)
                    }
                })
            }
            loadApp(e) {
                $.ajax(this.APP_LOAD_URL + e, {
                    success: e=>{
                        $("head").append(e)
                    }
                })
            }
            createAppHTML() {
                const e = document.createElement("div");
                return this.baseHTMLElement.appendChild(e),
                e
            }
            loadApplicationList() {
                $.ajax(this.APP_LIST_URL, {
                    success: e=>{
                        JSON.parse(e).forEach(e=>{
                            console.log(e);
                            const t = e.name;
                            this.loadApp(t)
                        }
                        )
                    }
                })
            }
            applyQueryResponse(e, t, i, n) {
                const r = JSON.parse(i);
                s.QueryDefinition.SetResponseVals(e, r),
                t.queryComplete(e)
            }
            startAppLoop() {
                this.mainLoopId = setInterval(this.appLoop, 5e3)
            }
            appLoop() {
                for (let e in this.registeredApps) {
                    if (!this.registeredApps.hasOwnProperty(e))
                        continue;
                    const t = this.registeredApps[e];
                    !t.IsWaitingQuery && t.HasBeenLoaded && t.App.clientOnly()
                }
            }
            sendRequestLoop() {
                0 != this.requests.length && this.requests.pop()
            }
            requestQueryCallback(e, ...t) {
                const s = t[0];
                $.ajax(s.URL, {
                    data: s.getParams(),
                    success: this.applyQueryResponse.bind(this, s, t[1])
                })
            }
            attachEventHandlers() {
                $(document).on("RequestQuery", $.proxy(this.requestQueryCallback, this))
            }
        }
    }
    .apply(t, i)) || (e.exports = n)
}
]);
