import { App } from "../Framework/App";
import {WindowAPI} from "./API/WindowAPI";
import { AppStatus } from "./AppStatus";
import { AppUIConfig } from "./AppUIConfig";
import { Logger } from "./Logger";
import {Logging } from "./Logging";
import { MagicMirrorConfig, MirrorConfigValues } from "./MagicMirrorConfig";
import { DeviceInfo } from "./Models/DeviceInfo";
import { PersistentSettings, PersistentSettingsLoader } from "./Models/PersistentSettings";
import { QueryDefinition } from "./QueryDefinition";
import { RegisteredApplicationRepository } from "./RegisteredAppRepo";
import { TimerTracker } from "./TimerTracker";
import { UIStack } from "./UIStack";
type RequestQueue = QueryDefinition[];

// tslint:disable-next-line: interface-name
interface AppDef {
    name: string;
    [key: string]: any;
    StartRow: number;
    EndRow: number;
    StartColumn: number;
    EndColumn: number;
    Priority: number;
}

class WindowBase {
    private logger = Logger.Instance;
    private timerContainer = new TimerTracker();
    private SettingsLoader: PersistentSettingsLoader = new PersistentSettingsLoader();
    private SavedSettings: PersistentSettings = this.SettingsLoader.LoadSettings();
    private baseHTMLElement: HTMLElement;
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

    public startLoadingSequence(): void {
        this.logger.LogInformational("Start Loading Sequence");
        this.loadDeviceInformationStep();
    }

    public loadDeviceInformationStep() {
        this.logger.LogInformational("Loading Device Information");
        const query = this.LoadDeviceInformation();
        query.then((data: any) => {
            this.logger.LogInformational("Device Information Loaded");
            this.onDeviceInfoLoaded(data);
            this.loadConfigStep();
        });
        query.fail( () => {
            this.logger.LogError("Error occured while loading device information");
            if ( this.SavedSettings.magicMirrorId) {
                this.logger.LogInformational("Invalid device id found. Creating new device.");
                this.SavedSettings.magicMirrorId = "";
                this.loadDeviceInformationStep();
                // this.SettingsLoader.SaveSettings(this.SavedSettings);
            }
        });
    }

    public loadConfigStep() {
        this.logger.LogInformational("Load Mirror Configuration");
        const query = WindowAPI.GetMagicMirrorConfig();
        query.then((data: any) => {
            this.logger.LogInformational("Loaded Mirror Configuration");
            this.applyMagicMirrorConfig(data);
            this.loadApplicationStep();
        });
        query.fail( () => {
            this.logger.LogError("Error occured while loading mirror configuration");
        });
    }
    public loadApplicationStep() {
        this.logger.LogInformational("Load mirror applications");
        const query = WindowAPI.GetApplicationList();
        query.then( (data: any) => {
            this.logger.LogInformational("Loaded mirror applications");
            this.setupApplicationList(data);
        });
        query.fail( () => {
            this.logger.LogError("Error occured while loading applications");
        });
    }

    public applyMagicMirrorConfig(data: any): void {
        if (!this.Device) { return; }
        const configData = JSON.parse(data);
        this.setupMirror({
            columns: configData.rows,
            heightUnit: this.Device.heightUnit,
            heightValue: this.Device.heightValue,
            rows: configData.rows,
            widthUnit: this.Device.widthUnit,
            widthValue: this.Device.widthValue,
        });
    }

    public LoadDeviceInformation(): JQuery.jqXHR {
        const savedId = this.SavedSettings.magicMirrorId;
        let query: JQuery.jqXHR | null = null;
        if (!savedId) {
            query = this.createDevice(document);
        } else {
            query = WindowAPI.GetDeviceInformation(savedId, undefined, undefined);
        }
        return query;
    }

    public getMagicMirrorConfig(data: any, textStatus: string, jqXHR: JQuery.jqXHR ): JQuery.jqXHR {
        const configQuery = $.ajax(this.CONFIG_URL);
        configQuery.done(this.applyMagicMirrorConfig.bind(this));
        return configQuery;
    }

    public getApplicationList(onComplete: JQuery.Ajax.SuccessCallback<any>) {
        return Logging.ajaxQueryWithLogging(this.APP_LIST_URL, onComplete, null);
    }

    public createDevice(doc: Document): JQuery.jqXHR {
        this.Device = new DeviceInfo(doc);
        return WindowAPI.CreateDevice(this.Device, undefined);
    }

    public onDeviceInfoLoaded(data: any): void {
        const parsedDevice = JSON.parse(data);
        this.logger.LogInformational(`Device Id ${parsedDevice.id} loaded`);
        this.Device = new DeviceInfo(data);
        if (this.Device == null) { return; }
        this.SavedSettings.magicMirrorId = this.Device.id;
        // this.SettingsLoader.SaveSettings(this.SavedSettings);
        document.head.appendChild(this.Device.TranslateToHTML());
        WindowAPI.DeviceLogin(this.Device, undefined);
    }

    public setupApplicationList(data: any): void {
        const response: AppDef[] = JSON.parse(data);
        response.forEach( (app: AppDef) => {
            this.logger.LogInformational(`Setting up application ${app.name}`);
            this.setupApplication(app);
        });
    }

    public setupApplication(app: AppDef) {
        const appName = app.name;
        this.registeredApps.RegisterApplication(appName);
        this.registeredApps.SetUIConfig(appName, AppUIConfig.ParseFromObject(app));
        this.loadApp(appName);
    }

    public setupMirror(config: MirrorConfigValues) {
        this.logger.LogInformational(`Creating mirror with ${config.rows} rows, ${config.columns} columns, width of ${config.widthValue}${config.widthUnit}, and height of ${config.heightValue}${config.heightUnit}`);
        this.uiStack = new UIStack(config.rows, config.columns);
        this.MirrorConfig = new MagicMirrorConfig(config);
        document.head.appendChild(this.MirrorConfig.TranslateToHTML());
    }

    public applyUIConfig(configVals: AppUIConfig, element: HTMLElement | any) {
        configVals.ApplyConfigToHTMLElement(element);
    }

    public addApplication(newApp: App): void {
        const appName = newApp.getName();
        this.registeredApps.SetupApplication(appName, newApp);
        this.startApps();
    }

    public addAppToUI(appName: string) {
        const appStatus: AppStatus | null = this.registeredApps.GetStatus(appName);
        const appUIStatus: AppUIConfig | null = this.registeredApps.GetUIConfig(appName);
        if (appStatus == null || appUIStatus == null) { return; }
        this.uiStack.PushApp(appStatus.App, appUIStatus);
    }

    public startApps(): void {
        if (!this.registeredApps.HaveAllAppsBeenLoaded()) { return; }
        const secondaryAppList = this.registeredApps.GetAppsWhereUI((app: AppUIConfig) => !app.LoadOnStart);
        const importantAppList = this.registeredApps.GetAppsWhereUI((app: AppUIConfig) => app.LoadOnStart);
        secondaryAppList.forEach(this.addAppToUI.bind(this));
        importantAppList.forEach(this.addAppToUI.bind(this));
        this.refreshAppsInUI();
    }
    public refreshAppsInUI(): void {
        const appList = this.uiStack.GetAppsToRender();
        for (const property in appList) {
            if (!appList.hasOwnProperty(property)) {
                continue;
            }
            const application = appList[property];
            const appUIConfig: AppUIConfig | null = this.registeredApps.GetUIConfig(property);
            const appStatus: AppStatus | null = this.registeredApps.GetStatus(property);
            if (!application || !appStatus || !appUIConfig || appStatus.HasBeenLoaded) { return; }
            application.OnCreate(this.timerContainer);
            if (application.clientOnly()) {
                this.startAppUI(application, appUIConfig, appStatus, null);
            } else {
                const UIQuery = application.getUIQuery();
                Logging.ajaxQueryWithLogging(UIQuery.URL,
                    this.startAppUI.bind(this, application, appUIConfig, appStatus), null);
            }
        }
    }

    public startAppUI(app: App, UIConfig: AppUIConfig, appStatus: AppStatus, data: any): void {
        const appHTMLElement = this.createAppHTML(app);
        if (data != null) {
            $(appHTMLElement).append(data);
        }
        this.applyUIConfig(UIConfig, appHTMLElement);
        app.onInitialRender(appHTMLElement);
        appStatus.HasBeenLoaded = true;
    }

    public loadApp(appName: string): void {
        Logging.ajaxQueryWithLogging(
            this.APP_LOAD_URL + appName,
            (data: any) => { $("head").append(data); },
            null,
        );
    }

    public createBaseAppContainer(): HTMLElement {
        const baseContainer = document.createElement("div");
        baseContainer.classList.add("magicMirrorContainer");
        baseContainer.classList.add("mirrorContainer");
        return baseContainer;
    }

    public createAppHTML(app: App): HTMLElement {
        const appContainer = document.createElement("div");
        appContainer.classList.add("magicMirrorApp");
        appContainer.setAttribute("data-MagicMirrorAppID", app.getName());
        this.baseHTMLElement.appendChild(appContainer);
        return appContainer;
    }

    public applyQueryResponse(queryDef: QueryDefinition, owningApp: App, data?: any, status?: string) {
        let dataObject = data;
        if (typeof data === "string") {
            dataObject = JSON.parse(data);
        }
        QueryDefinition.SetResponseVals(queryDef, dataObject);
        owningApp.queryComplete(queryDef);
    }

    public sendRequestLoop(): void {
        if (this.requests.length === 0) { return; }
        const currentRequest = this.requests.pop();
        if (!currentRequest) { return; }
    }

    public requestQueryCallback(event: any, ...params: any[]): void {
        const requestedQuery = params[0] as QueryDefinition;
        const url = this.SERVER_URL + requestedQuery.URL;

        Logging.ajaxQueryWithLogging(url,
            this.applyQueryResponse.bind(this, requestedQuery, params[1]), null);
    }

    public requestCloseApplication(event: any, ...params: any[]): void {
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

    public attachEventHandlers(): void {
        $(document).on("RequestQuery", $.proxy(this.requestQueryCallback, this));
        $(document).on("RequestClose", $.proxy(this.requestCloseApplication, this));
    }
}

const startFunction = (global: any) => {
    global.MagicMirror = new WindowBase();
};
startFunction(window);
