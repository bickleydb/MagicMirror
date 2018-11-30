import {App} from '../Framework/App'
import { QueryDefinition } from '../Framework/QueryDefinition';
import { ApplicationEventEnum, ApplicationRequestEnum } from '../Framework/AppEventsEnum';

export class MultiApp extends App {

    private ChildApps : App[] | null = null;


     clientOnly() : boolean {
         return false;
     }

     getName() : string {
         return "MultiApp";
     }

     onInit () : void {
        return;
     }

     getUIQuery() : QueryDefinition {
        return new QueryDefinition("");
     }

     onInitialRender(parent_element : HTMLElement) : void {

     }
     
     queryComplete(queryDef : QueryDefinition) : void {

     }

}