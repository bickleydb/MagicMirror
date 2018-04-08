import { QueryDefinition } from './QueryDefinition';
import { EventManager } from '../Common/EventManager';
import { AppStatus } from './AppStatus';
import {App} from "../Framework/App"
import { AppUIConfig } from './AppUIConfig';



type RequestQueue = QueryDefinition[];


interface AppDef {
    name : string,
    [key:string] : string 
}

class WindowBase {
    private baseHTMLElement : HTMLElement

    private registeredApps : { [key:string] : AppStatus };
    private AppUIConfig : { [key:string] : AppUIConfig };

    private requests : RequestQueue;
    private requestTimer : number = -1;

    private mainLoopId : number = -1;


    private readonly SERVER_URL = "http://127.0.0.1:8000";

    private readonly START_URL = this.SERVER_URL + "/startup/";
    private readonly APP_LIST_URL = this.SERVER_URL + "/loadApplications";
    private readonly APP_LOAD_URL = this.SERVER_URL + "/loadApp/";
    private readonly CONFIG_URL = this.SERVER_URL + "/loadConfiguration";

    constructor() {
        this.baseHTMLElement = this.createBaseAppContainer();  
        document.body.appendChild(this.baseHTMLElement);    
        this.requests = [];
        this.AppUIConfig = {};
        this.registeredApps = {};

       // this.loadApplicationList();
        this.attachEventHandlers();

       this.startLoadingSequence();
    }


    startLoadingSequence() : void {
        const configQuery =  $.ajax(this.CONFIG_URL);
        configQuery.done( (data:any) => { this.setupConfig(JSON.parse(data));})
        const nextQuery = configQuery.then( () => {return $.ajax(this.APP_LIST_URL);})
        nextQuery.done( (data:any) => {
            let response : AppDef[] = JSON.parse(data);
            response.forEach(app => {
                const UIConfig = new AppUIConfig();
                UIConfig.RowStart = parseInt(app.startRow);
                UIConfig.RowEnd = parseInt(app.endRow);
                UIConfig.ColumnStart = parseInt(app.startColumn);
                this.AppUIConfig[app.name] = UIConfig;
                UIConfig.ColumnEnd = parseInt(app.endColumn);
                const appName = app.name;
                this.loadApp(appName);
            });      
        })
    }

    setupConfig(config : {rows : number, columns : number, widthValue : number, widthUnit:string, heightValue:number, heightUnit:string}) {
        const inlineElement = document.createElement("style");
        inlineElement.innerText = ".mirrorContainer { " + "width:" + config.widthValue + config.widthUnit  + "; height:" + config.heightValue + config.heightUnit + ";" + "grid-template-rows:" +  ((100/config.rows)+"% ").repeat(config.rows) + ";" + "grid-template-columns:" + ((100/config.columns)+"% ").repeat(config.columns) + ";" + "</style>"
        document.head.appendChild(inlineElement);
    }

    applyUIConfig(configVals : AppUIConfig, element : HTMLElement | any) 
    {      
        element.style.gridRowStart = configVals.RowStart;
        element.style.gridRowEnd = configVals.RowEnd;
        element.style.gridColumnStart = configVals.ColumnStart;
        element.style.gridColumnEnd = configVals.ColumnEnd;

        if(element instanceof HTMLElement) {
            const containerRect = element.getBoundingClientRect();
            element.style.fontSize = containerRect.width + "px";
            element.style.width = containerRect.width + "px";
            element.style.height = containerRect.height + "px";
            element.style.position = "relative";
        }
    }

    addApplication(newApp : App) : void  {
        const appName = newApp.getName();
        this.registeredApps[appName] = new AppStatus(newApp);
        const appUI = this.AppUIConfig[newApp.getName()];
    
        
        if(newApp.clientOnly()) {
            const curElement = this.createAppHTML();
            newApp.onInitialRender(curElement);
            this.applyUIConfig(appUI, curElement);
            return;
        }
        const UIQuery = newApp.getUIQuery();
        $.ajax(UIQuery.URL, {
            success : (data:any) => {
                const appHTMLElement = this.createAppHTML();
                $(appHTMLElement).append(data);
                this.applyUIConfig(appUI, appHTMLElement);
                newApp.onInitialRender(appHTMLElement);
            }
        })
    }

    loadApp(appName: string) : void {
        $.ajax(this.APP_LOAD_URL + appName, {
            success : (data:any) =>  {
                $("head").append(data);
            }
         });
    }

    createBaseAppContainer() : HTMLElement {
        const baseContainer = document.createElement("div");
        baseContainer.classList.add("magicMirrorContainer");
        baseContainer.classList.add("mirrorContainer");
        return baseContainer;
    }

    createAppHTML() : HTMLElement {
        const appContainer = document.createElement("div");
        appContainer.classList.add("magicMirrorApp");
        this.baseHTMLElement.appendChild(appContainer);
        return appContainer;
    }

    loadApplicationList() : void {
        $.ajax(this.APP_LIST_URL, {
            success : (data:any) => {
                    let response : AppDef[] = JSON.parse(data);
                    response.forEach(app => {
                        const appName = app.name;
                        alert(app)
                        this.loadApp(appName);
                    });      
                }
        });
    }


    applyQueryResponse(queryDef : QueryDefinition, owningApp : App,  data? : any, status?:string)  {
        const dataObject = JSON.parse(data);
        QueryDefinition.SetResponseVals(queryDef,dataObject);
        owningApp.queryComplete(queryDef);
    }
    

    startAppLoop() : void {
        this.mainLoopId = setInterval(this.appLoop, 5000);
    }

    appLoop() : void {
        for(let property in this.registeredApps) {
            if(!this.registeredApps.hasOwnProperty(property)) {continue;}
            const appStatus = this.registeredApps[property];
            if(appStatus.IsWaitingQuery || !appStatus.HasBeenLoaded || appStatus.App.clientOnly()) {continue;}
        }
    }



    setupMagicMirror(data : object) : void {

    }


    sendRequestLoop() : void {
        if(this.requests.length == 0) {return;}
        let currentRequest = this.requests.pop();
        if(!currentRequest){return;}
    }

    requestQueryCallback(event : any, ...params : any[]) : void { 
        const requestedQuery = params[0] as QueryDefinition;
        $.ajax(requestedQuery.URL, {
            data : requestedQuery.getParams(),
            success: this.applyQueryResponse.bind(this, requestedQuery, params[1]),
        });
    }

    attachEventHandlers() : void {
        $(document).on("RequestQuery", $.proxy(this.requestQueryCallback,this));
    }
}
    

(function (global:any) {
    global.MagicMirror = new WindowBase();
}(window));