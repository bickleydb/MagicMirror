import { QueryDefinition } from './QueryDefinition';
import { EventManager } from '../Common/EventManager';
import { AppStatus } from './AppStatus';
import {App} from "../Framework/App"



type RequestQueue = QueryDefinition[];


interface AppDef {
    name : string,
    other: { [key:string] : string }
}

class WindowBase {
    private baseHTMLElement : HTMLElement

    private registeredApps : { [key:string] : AppStatus };
  

    private requests : RequestQueue;
    private requestTimer : number = -1;

    private mainLoopId : number = -1;

    private readonly START_URL = "http://127.0.0.1:8000/startup/";
    private readonly APP_LIST_URL = "http://127.0.0.1:8000/loadApplications";
    private readonly APP_LOAD_URL = "http://127.0.0.1:8000/loadApp/";

    constructor() {
        this.baseHTMLElement = document.body;        
        this.requests = [];
        this.registeredApps = {};

        this.loadApplicationList();
        this.attachEventHandlers();
    }

    addApplication(newApp : App) : void  {
        const appName = newApp.getName();
        this.registeredApps[appName] = new AppStatus(newApp);
        if(newApp.clientOnly()) {
            newApp.onInitialRender(this.createAppHTML());
            return;
        }
        const UIQuery = newApp.getUIQuery();
        $.ajax(UIQuery.URL, {
            success : (data:any) => {
                const appHTMLElement = this.createAppHTML();
                $(appHTMLElement).append(data);
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

    createAppHTML() : HTMLElement {
        const appContainer = document.createElement("div");
        this.baseHTMLElement.appendChild(appContainer);
        return appContainer;
    }

    loadApplicationList() : void {
        $.ajax(this.APP_LIST_URL, {
            success : (data:any) => {
                    let response : AppDef[] = JSON.parse(data);
                    response.forEach(app => {
                        const appName = app.name;
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


    sendRequestLoop() : void {
        if(this.requests.length == 0) {return;}
        let currentRequest = this.requests.pop();
        if(!currentRequest){return;}
      /*  $.ajax(currentRequest.URL, {
            data : currentRequest.getParams(),
            success: this.applyQueryResponse.bind(this, currentRequest),
        });*/
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