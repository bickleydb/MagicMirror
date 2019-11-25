import {App} from "../Framework/App";
import { AppStatus } from "./AppStatus";
import { AppUIConfig } from "./AppUIConfig";

type AppUIBoolFunc = (configObj: AppUIConfig)  => boolean;

export class RegisteredApplicationRepository {

    private RegisteredAppList: {[key: string]: boolean};
    private ApplicationStatus: {[key: string]: AppStatus | null};
    private ApplicationUIConfig: {[key: string]: AppUIConfig | null};

    constructor() {
        this.ApplicationStatus = {};
        this.ApplicationUIConfig = {};
        this.RegisteredAppList = {};
    }

    public RegisterApplication(key: string): void {
        this.RegisteredAppList[key] = false;
        this.ApplicationStatus[key] = null;
        this.ApplicationUIConfig[key] = null;
    }

    public SetupApplication(key: string, application: App, startingUI?: AppUIConfig | null): void {
        this.RegisteredAppList[key] = true;
        this.ApplicationStatus[key] = new AppStatus(application);

        if (typeof this.ApplicationUIConfig[key] === "undefined" && typeof startingUI !== "undefined") {
            this.ApplicationUIConfig[key] = startingUI;
        }
    }

    public SetUIConfig(key: string, config: AppUIConfig): void {
        if (!this.HasBeenRegistered(key)) {throw new Error("App " + key + " has not been registered."); }
        this.ApplicationUIConfig[key] = config;
    }

    public GetStatus(key: string): AppStatus | null {
        if (!this.HasBeenRegistered(key)) {throw new Error("App " + key + " has not been registered."); }
        return this.ApplicationStatus[key];
    }

    public GetUIConfig(key: string): AppUIConfig | null {
        if (!this.HasBeenRegistered(key)) {throw new Error("App " + key + " has not been registered."); }
        return this.ApplicationUIConfig[key];
    }

    public HasAppBeenLoaded(key: string) {
        if (!this.HasBeenRegistered(key)) {throw new Error("App " + key + " has not been registered."); }
        return this.RegisteredAppList[key];
    }

    public RemoveApp(key: string) {
        delete this.ApplicationStatus[key];
        delete this.ApplicationUIConfig[key];
    }

    public GetAppsWhereUI( func: AppUIBoolFunc): string[] {
        const appList = [];
        for (const property in this.RegisteredAppList) {
            if (!this.RegisteredAppList.hasOwnProperty(property)) {continue; }
            const uiConfig = this.ApplicationUIConfig[property];
            if (!uiConfig) {continue; }
            if (func.call(this, uiConfig)) {
                appList.push(property);
            }
        }
        return appList;
    }

    public HaveAllAppsBeenLoaded(): boolean {
        for (const property in this.RegisteredAppList) {
            if (!this.RegisteredAppList.hasOwnProperty(property)) {continue; }
            if (!this.RegisteredAppList[property]) {return false; }
        }
        return true;
    }

    private HasBeenRegistered(key: string): boolean {
        if (typeof this.RegisteredAppList[key] === "undefined") {
            return false;
        }
        return true;
    }

}
