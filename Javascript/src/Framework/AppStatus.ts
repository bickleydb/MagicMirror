import {App} from "./App";

export class AppStatus {

    private hasBeenLoaded : boolean;
    private isWaitingQuery : boolean;
    private isWaitingOnInit : boolean;
    private isVisible : boolean;
    private app : App;

    public constructor(app: App) {
        this.app = app;
        this.hasBeenLoaded = false;
        this.isWaitingQuery = false;
        this.isWaitingOnInit = false;
        this.isVisible = false;
    }

    public get App() : App{
        return this.app;
    }

    public get HasBeenLoaded() : boolean {
        return this.hasBeenLoaded;
    }

    public get IsWaitingQuery() : boolean {
        return this.isWaitingQuery;
    }

    public get IsWaitingOnInit() : boolean {
        return this.isWaitingOnInit;
    }

    public get IsVisible() : boolean {
        return this.isVisible;
    }

    public set IsWaitingOnInit(isWaiting : boolean) {
        this.isWaitingOnInit = isWaiting;
    }

    public set IsVisible(value:boolean) {
        this.isVisible = value;
    }


    public set App(app:App) {
        this.app = app;
    }

    public set HasBeenLoaded(hasBeenLoaded: boolean)  {
        this.hasBeenLoaded = hasBeenLoaded;
    }

    public set IsWaitingQuery(isWaiting : boolean)  {
        this.IsWaitingQuery = isWaiting;
    }
}
