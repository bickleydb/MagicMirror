import * as $ from "jquery";

export class EventManager {

    public static TriggerEvent(eventName: string , ...params: any[]): void {
        $(EventManager.TARGET).trigger(eventName, params);
    }
    // tslint:disable-next-line: ban-types
    public static AddEventListener(eventList: string , resultFunction: Function , context: any): void {
        $(EventManager.TARGET).on(eventList, null, null, $.proxy(resultFunction, context));
    }

    private static TARGET = "MagicMirror";
}
