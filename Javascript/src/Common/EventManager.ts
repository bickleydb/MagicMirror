import * as $ from 'jquery'


export class EventManager {

    private static TARGET = "MagicMirror";


    static TriggerEvent(eventName : string , ...params : any[]): void {
        $(EventManager.TARGET).trigger(eventName, params);
    }
    static AddEventListener(eventList : string , resultFunction : Function , context : any) : void {
        $(EventManager.TARGET).on(eventList, null, null, $.proxy(resultFunction, context));
    }
}