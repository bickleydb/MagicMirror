import { Logger } from "./Logger";

// tslint:disable-next-line: interface-name
interface Timer {
    TimerName: string;
    TimerId: number;
    Interval: number;
    // tslint:disable-next-line: ban-types
    Callback: Function;
    StopTimer: boolean;
    CancelTimer: boolean;
}

// tslint:disable-next-line: interface-name
interface TimerDictionary {
    [timerName: string]: Timer;
}

export class TimerTracker {

    private timerList: TimerDictionary;

    constructor() {
        this.timerList = {};
    }

    // tslint:disable-next-line: ban-types
    public SetInterval(timerName: string, millisecondInterval: number, callback: Function): void {
        if (this.timerList[timerName]) {
            throw new Error("Timer has already been created.");
        }

        const timerInstance: Timer = {
            Callback: callback,
            CancelTimer: false,
            Interval: millisecondInterval,
            StopTimer: false,
            TimerId: setTimeout(() => {this.OnInterval(timerName); }, millisecondInterval),
            TimerName : timerName,
        };
        this.timerList[timerName] = timerInstance;
    }

    private OnInterval(timerName: string): void {
        const currentTimer = this.timerList[timerName];
        if (currentTimer.CancelTimer) {
            Logger.Instance.LogInformational(`Timer ${currentTimer.TimerName} was cancelled.`);
            return;
        }
        Logger.Instance.LogInformational(`Timer ${currentTimer.TimerName} was invoked.`);
        currentTimer.Callback();
        if (currentTimer.StopTimer) {
            Logger.Instance.LogInformational(`Timer ${currentTimer.TimerName} was stopped.`);
            return;
        }
        currentTimer.TimerId = setTimeout(() => {this.OnInterval(timerName); }, currentTimer.Interval);
        Logger.Instance.LogInformational(`Timer ${currentTimer.TimerName} has been scheduled.`);
    }
}
