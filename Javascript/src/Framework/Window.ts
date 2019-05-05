import { MagicMirrorConfig } from './MagicMirrorConfig';
import { QueryDefinition } from './QueryDefinition';
import { EventManager } from '../Common/EventManager';
import { AppStatus } from './AppStatus';
import { App } from "../Framework/App"
import { AppUIConfig } from './AppUIConfig';
import { RegisteredApplicationRepository } from './RegisteredAppRepo';
import { UIStack } from './UIStack';
import { Logging } from './Logging';
import { DeviceInfo } from './Models/DeviceInfo';
import { PersistentSettings, PersistentSettingsLoader } from './Models/PersistentSettings';

type RequestQueue = QueryDefinition[];


interface AppDef {
    name: string,
    [key: string]: any,
    StartRow: number,
    EndRow: number,
    StartColumn: number,
    EndColumn: number,
    Priority: number
}

class WindowBase {

    private SettingsLoader: PersistentSettingsLoader = new PersistentSettingsLoader();
    private SavedSettings: PersistentSettings = this.SettingsLoader.LoadSettings();

    private baseHTMLElement: HTMLElement
    private registeredApps: RegisteredApplicationRepository;
    private AppUIConfig: { [key: string]: AppUIConfig };

    private requests: RequestQueue;
    private uiStack: UIStack = new UIStack(0, 0);
    private MirrorConfig: MagicMirrorConfig | null = null;
    private Device: DeviceInfo | null = null;

    private readonly SERVER_URL = "";
    private readonly APP_LIST_URL = this.SERVER_URL + "/loadApplications";
    private readonly APP_LOAD_URL = this.SERVER_URL + "/loadApp/";
    private readonly CONFIG_URL = this.SERVER_URL + "/loadConfiguration";
    private readonly DEVICE_URL = this.SERVER_URL + "/loadDeviceData?deviceId=";
    private readonly DEVICE_CREATE_URL = this.SERVER_URL + "/devicecreate";

    constructor() {
        this.baseHTMLElement = this.createBaseAppContainer();
        document.body.appendChild(this.baseHTMLElement);
        this.requests = [];
        this.AppUIConfig = {};
        this.registeredApps = new RegisteredApplicationRepository();
        this.attachEventHandlers();
        this.startLoadingSequence();
    }

    startLoadingSequence(): void {
        this.SettingsLoader.LoadSettings();
        this.getDeviceInformation(
            this.onDeviceInfoLoaded.bind(this, this.getMagicMirrorConfig));
        this.getApplicationList(this.setupApplicationList.bind(this));
    }

    applyMagicMirrorConfig(onSuccess: Function, data: any): void {
        if (!this.Device) { return; }
        const configData = JSON.parse(data);
        this.setupMirror({
            "rows": configData.rows,
            "columns": configData.rows,
            "widthValue": this.Device.width_value,
            "widthUnit": this.Device.width_unit,
            "heightValue": this.Device.height_value,
            "heightUnit": this.Device.height_unit,
        })
        onSuccess.call(this);
    }

    getMagicMirrorConfig(onSuccess: Function): JQuery.jqXHR {
        const configQuery = $.ajax(this.CONFIG_URL);
        configQuery.done(this.applyMagicMirrorConfig.bind(this, onSuccess));
        return configQuery;
    }

    getApplicationList(onComplete: JQuery.Ajax.SuccessCallback<any>) {
        return Logging.ajaxQueryWithLogging(this.APP_LIST_URL, onComplete, null);
    }

    createDevice(onComplete: JQuery.Ajax.SuccessCallback<any> | null, doc: Document): JQuery.jqXHR | null {
        this.Device = new DeviceInfo(doc);
        return Logging.ajaxQueryWithLoggingSettings({
            url: this.DEVICE_CREATE_URL,
            method: "POST",
            data: JSON.stringify(this.Device),
            success: (data: any) => {
                const parsedDevice = JSON.parse(data);
                this.SavedSettings.magicMirrorDeviceId = parsedDevice.id;
                this.SettingsLoader.SaveSettings(this.SavedSettings);
                console.log("Device Id " + parsedDevice.id + " loaded");
                if(onComplete != null) {
                    this.onDeviceInfoLoaded(onComplete, data);
                }
            },
            error: () => { }
        })
    }

    onDeviceInfoLoaded(callback: Function, data: any): void {
        this.Device = new DeviceInfo(data);
        if (this.Device == null) { return; }
        document.head.appendChild(this.Device.TranslateToHTML());
        console.log(this.Device);
        callback.call(this, data);
    }

    getDeviceInformation(onComplete: JQuery.Ajax.SuccessCallback<any> | null): JQuery.jqXHR | null {
        const savedId = this.SavedSettings.magicMirrorDeviceId;
        let onSuccess = onComplete;
        if (onSuccess == null) {
            onSuccess = () => { };
        }
        if (!savedId) {
            return this.createDevice(onSuccess,document);
        } else {
            return Logging.ajaxQueryWithLoggingSettings({
                url: this.DEVICE_URL + savedId,
                success: onSuccess,
                error: (data: any) => { console.error(data); }
            });
        }
    }

    setupApplicationList(data: any): void {
        let response: AppDef[] = JSON.parse(data);
        response.forEach(this.setupApplication.bind(this));
    }

    setupApplication(app: AppDef) {
        const appName = app.name;
        this.registeredApps.RegisterApplication(appName);
        this.registeredApps.SetUIConfig(appName, AppUIConfig.ParseFromObject(app));
        this.loadApp(appName);
    }

    setupMirror(config: { rows: number, columns: number, widthValue: number, widthUnit: string, heightValue: number, heightUnit: string }) {
        this.uiStack = new UIStack(config.rows, config.columns);
        this.MirrorConfig = new MagicMirrorConfig(config);
        document.head.appendChild(this.MirrorConfig.TranslateToHTML());
    }

    applyUIConfig(configVals: AppUIConfig, element: HTMLElement | any) {
        configVals.ApplyConfigToHTMLElement(element);
    }

    addApplication(newApp: App): void {
        const appName = newApp.getName();
        this.registeredApps.SetupApplication(appName, newApp);
        this.startApps();
    }

    addAppToUI(appName: string) {
        const appStatus: AppStatus | null = this.registeredApps.GetStatus(appName);
        const appUIStatus: AppUIConfig | null = this.registeredApps.GetUIConfig(appName);
        if (appStatus == null || appUIStatus == null) { return; }
        this.uiStack.PushApp(appStatus.App, appUIStatus);
    }


    startApps(): void {
        if (!this.registeredApps.HaveAllAppsBeenLoaded()) { return; }
        const secondaryAppList = this.registeredApps.GetAppsWhereUI((app: AppUIConfig) => { return !app.LoadOnStart });
        const importantAppList = this.registeredApps.GetAppsWhereUI((app: AppUIConfig) => { return app.LoadOnStart });
        secondaryAppList.forEach(this.addAppToUI.bind(this));
        importantAppList.forEach(this.addAppToUI.bind(this));
        this.refreshAppsInUI();
    }
    refreshAppsInUI(): void {
        const appList = this.uiStack.GetAppsToRender();
        for (var property in appList) {
            if (!appList.hasOwnProperty(property)) {
                continue;
            }
            const application = appList[property];
            const appUIConfig: AppUIConfig | null = this.registeredApps.GetUIConfig(property);
            const appStatus: AppStatus | null = this.registeredApps.GetStatus(property);
            if (!application || !appStatus || !appUIConfig || appStatus.HasBeenLoaded) { return; }
            if (application.clientOnly()) {
                this.startAppUI(application, appUIConfig, appStatus, null);
            } else {
                const UIQuery = application.getUIQuery();
                Logging.ajaxQueryWithLogging(UIQuery.URL, this.startAppUI.bind(this, application, appUIConfig, appStatus), null);
            }
        }
    }

    startAppUI(app: App, UIConfig: AppUIConfig, appStatus: AppStatus, data: any): void {
        const appHTMLElement = this.createAppHTML(app);
        if (data != null) {
            $(appHTMLElement).append(data);
        }
        this.applyUIConfig(UIConfig, appHTMLElement);
        app.onInitialRender(appHTMLElement);
        appStatus.HasBeenLoaded = true;
    }

    loadApp(appName: string): void {
        Logging.ajaxQueryWithLogging(
            this.APP_LOAD_URL + appName,
            (data: any) => { $("head").append(data); },
            null
        );
    }

    createBaseAppContainer(): HTMLElement {
        const baseContainer = document.createElement("div");
        baseContainer.classList.add("magicMirrorContainer");
        baseContainer.classList.add("mirrorContainer");
        return baseContainer;
    }

    createAppHTML(app: App): HTMLElement {
        const appContainer = document.createElement("div");
        appContainer.classList.add("magicMirrorApp");
        appContainer.setAttribute("data-MagicMirrorAppID", app.getName());
        this.baseHTMLElement.appendChild(appContainer);
        return appContainer;
    }


    applyQueryResponse(queryDef: QueryDefinition, owningApp: App, data?: any, status?: string) {
        let dataObject = data;
        if (typeof data === "string") {
            dataObject = JSON.parse(data);
        }
        QueryDefinition.SetResponseVals(queryDef, dataObject);
        owningApp.queryComplete(queryDef);
    }

    sendRequestLoop(): void {
        if (this.requests.length == 0) { return; }
        let currentRequest = this.requests.pop();
        if (!currentRequest) { return; }
    }

    requestQueryCallback(event: any, ...params: any[]): void {
        const requestedQuery = params[0] as QueryDefinition;
        const url = this.SERVER_URL + requestedQuery.URL;

        Logging.ajaxQueryWithLogging(url,
            this.applyQueryResponse.bind(this, requestedQuery, params[1]), null);
    }

    requestCloseApplication(event: any, ...params: any[]): void {
        const app = params[0] as App;
        const appNameString = app.getName();
        const appContainer = document.querySelector("[data-MagicMirrorAppID=\"" + appNameString + "\"]");
        if (appContainer && appContainer.parentElement) {
            appContainer.parentElement.removeChild(appContainer);
        }
        app.OnClose();
        this.registeredApps.RemoveApp(app.getName());
        this.uiStack.PopApp(app);
        this.refreshAppsInUI();
    }

    attachEventHandlers(): void {
        $(document).on("RequestQuery", $.proxy(this.requestQueryCallback, this));
        $(document).on("RequestClose", $.proxy(this.requestCloseApplication, this));
    }
}


(function (global: any) {
    global.MagicMirror = new WindowBase();
}(window));