import { ApplicationEventEnum, ApplicationRequestEnum } from './AppEventsEnum';
import * as $ from "jquery";
import { QueryDefinition } from './QueryDefinition';


export abstract class App {

    private has_been_destroyed = false;
    private has_been_created = false;

    constructor () {
       
    }

    abstract clientOnly() : boolean;
    abstract getName() : string; 
    abstract onInit () : void;
    abstract getUIQuery() : QueryDefinition;
    abstract onInitialRender(parent_element : HTMLElement) : void;   
    abstract queryComplete(queryDef : QueryDefinition) : void;


    onDestroy () : void {
        this.has_been_destroyed = true;
    }

    protected hasBeenCreated () : boolean {
        return this.has_been_created;
    }

    public OnCreate () : void {
    
    }

    public OnStart () : void {

    }
    
    public OnHide() : void {

    }
    
    public OnClose() : void {

    }

    public OnDestoy() : void {

    }

    


}