import { MagicMirrorConfig } from './MagicMirrorConfig';
import { QueryDefinition } from './QueryDefinition';
import { EventManager } from '../Common/EventManager';
import { AppStatus } from './AppStatus';
import {App} from "../Framework/App"
import { AppUIConfig } from './AppUIConfig';
import {RegisteredApplicationRepository} from './RegisteredAppRepo';
import { UIStack } from './UIStack';


type RequestQueue = QueryDefinition[];


interface AppDef {
    name : string,
    [key:string] : any, 
    StartRow:number, 
    EndRow:number,
    StartColumn:number,
    EndColumn:number,
    Priority:number
}

interface QueryResponseFunction {
    (data:any) : any 
}

class WindowBase {
    private baseHTMLElement : HTMLElement

    private registeredApps : RegisteredApplicationRepository;
    private AppUIConfig : { [key:string] : AppUIConfig };

    private requests : RequestQueue;
    private requestTimer : number = -1;

    private mainLoopId : number = -1;
    private uiStack : UIStack = new UIStack(0,0);
    private MirrorConfig : MagicMirrorConfig | null = null;


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
        this.registeredApps = new RegisteredApplicationRepository();
        this.attachEventHandlers();
        this.startLoadingSequence();
    }


    startLoadingSequence() : void {
        const MagicMirrorConfigQuery = this.getMagicMirrorConfig();
        const nextQuery = this. getApplicationList(MagicMirrorConfigQuery, this.setupApplicationList.bind(this));
    }

    getApplicationList(prevQuery : JQuery.jqXHR, onComplete : QueryResponseFunction ) {
        const appListQuery = prevQuery.then( () => {return $.ajax(this.APP_LIST_URL);})
        appListQuery.done(onComplete);
    }

    setupApplicationList(data:any)  : void {
        let response : AppDef[] = JSON.parse(data);
        response.forEach(this.setupApplication.bind(this));
    }

    getMagicMirrorConfig() {
        const configQuery =  $.ajax(this.CONFIG_URL);
        configQuery.done( (data:any) => { this.setupMirror(JSON.parse(data));})
        return configQuery;
    }

    setupApplication(app : AppDef) {
        const appName = app.name;
        this.registeredApps.RegisterApplication(appName);
        this.registeredApps.SetUIConfig(appName, AppUIConfig.ParseFromObject(app));
        this.loadApp(appName);
    }
    
    setupMirror(config : {rows : number, columns : number, widthValue : number, widthUnit:string, heightValue:number, heightUnit:string}) {
        this.uiStack = new UIStack(config.rows,config.columns);
        this.MirrorConfig = new MagicMirrorConfig(config);
        document.head.appendChild(this.MirrorConfig.TranslateToHTML());
    }

    applyUIConfig(configVals : AppUIConfig, element : HTMLElement | any) 
    {      
        configVals.ApplyConfigToHTMLElement(element);
    }

    addApplication(newApp : App) : void  {
        const appName = newApp.getName();
        this.registeredApps.SetupApplication(appName,newApp);
        this.startApps();
    }

    addAppToUI(appName: string) {
        const appStatus : AppStatus | null = this.registeredApps.GetStatus(appName);
        const appUIStatus : AppUIConfig | null = this.registeredApps.GetUIConfig(appName);
        if(appStatus == null || appUIStatus == null) {return;}
        this.uiStack.PushApp(appStatus.App,appUIStatus);
    }


    startApps() : void {
        if(!this.registeredApps.HaveAllAppsBeenLoaded()) {return;}
        const secondaryAppList = this.registeredApps.GetAppsWhereUI((app : AppUIConfig) => {return !app.LoadOnStart});
        const importantAppList = this.registeredApps.GetAppsWhereUI((app : AppUIConfig) => {return app.LoadOnStart});
        secondaryAppList.forEach(this.addAppToUI.bind(this));
        importantAppList.forEach(this.addAppToUI.bind(this));
        this.refreshAppsInUI();
    }

    

    refreshAppsInUI() : void {
        const appList  = this.uiStack.GetAppsToRender();
        for(var property in appList) {
            if(!appList.hasOwnProperty(property)) {
                continue;
            }
            const application = appList[property];
            const appUIConfig : AppUIConfig | null = this.registeredApps.GetUIConfig(property);
            const appStatus : AppStatus | null = this.registeredApps.GetStatus(property);
            if(!application || !appStatus || !appUIConfig || appStatus.HasBeenLoaded) {return;}
            if(application.clientOnly()) {
                this.startAppUI(application,appUIConfig,appStatus,null);
             } else {
                const UIQuery = application.getUIQuery();
                $.ajax(UIQuery.URL, {
                    success : this.startAppUI.bind(this,application, appUIConfig, appStatus)
                });
            }
        }
    }

    startAppUI(app:App, UIConfig : AppUIConfig,  appStatus : AppStatus, data:any) : void {
        const appHTMLElement = this.createAppHTML(app);
        if(data != null) {
            $(appHTMLElement).append(data);
        }
        this.applyUIConfig(UIConfig, appHTMLElement);
        app.onInitialRender(appHTMLElement);
        appStatus.HasBeenLoaded = true;
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

    createAppHTML(app:App) : HTMLElement {
        const appContainer = document.createElement("div");
        appContainer.classList.add("magicMirrorApp");
        appContainer.setAttribute("data-MagicMirrorAppID",app.getName());
        this.baseHTMLElement.appendChild(appContainer);
        return appContainer;
    }


    applyQueryResponse(queryDef : QueryDefinition, owningApp : App,  data? : any, status?:string)  {
        const dataObject = JSON.parse(data);
        QueryDefinition.SetResponseVals(queryDef,dataObject);
        owningApp.queryComplete(queryDef);
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
    
    requestCloseApplication(event : any, ...params : any[]) : void {
        const app = params[0] as App;
        const appNameString = app.getName();
        const appContainer = document.querySelector("[data-MagicMirrorAppID=\""+appNameString+"\"]");
        if(appContainer && appContainer.parentElement) {
            appContainer.parentElement.removeChild(appContainer);
        }
        app.OnClose();
        this.registeredApps.RemoveApp(app.getName());
        this.uiStack.PopApp(app);
        this.refreshAppsInUI();
    }

    attachEventHandlers() : void {
        $(document).on("RequestQuery", $.proxy(this.requestQueryCallback,this));
        $(document).on("RequestClose", $.proxy(this.requestCloseApplication,this));

    }
}
    

(function (global:any) {
    global.MagicMirror = new WindowBase();
}(window));