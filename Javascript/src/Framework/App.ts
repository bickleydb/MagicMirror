import { QueryDefinition } from "./QueryDefinition";
import { TimerTracker } from "./TimerTracker";

export abstract class App {

    private created = false;
    private timerTracker: TimerTracker | undefined;

    // tslint:disable-next-line: no-empty
    constructor() { }

    public abstract clientOnly(): boolean;
    public abstract getName(): string;
    public abstract onInit(): void;
    public abstract getUIQuery(): QueryDefinition;
    public abstract onInitialRender(parentElement: HTMLElement): void;
    public abstract queryComplete(queryDef: QueryDefinition): void;

    // tslint:disable-next-line: no-empty
    public onDestroy(): void { }

    public OnCreate(timerContainer: TimerTracker): void {
        this.timerTracker = timerContainer;
    }

    public CreateTimer(timeoutName: string, millisecondInterval: number, callback: () => void): void {
        if (!this.timerTracker) {return; }
        this.timerTracker.SetInterval(`${this.getName()}-${timeoutName}`, millisecondInterval, callback);
    }

    // tslint:disable-next-line: no-empty
    public OnStart(): void { }

    // tslint:disable-next-line: no-empty
    public OnHide(): void { }

    // tslint:disable-next-line: no-empty
    public OnClose(): void { }

    // tslint:disable-next-line: no-empty
    public OnDestoy(): void { }

    protected hasBeenCreated(): boolean {
        return this.created;
    }
}
