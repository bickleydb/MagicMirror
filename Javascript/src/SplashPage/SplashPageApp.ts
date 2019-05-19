import { SplashPageAppQuery } from './SplashPageAppQuery';
import { QueryDefinition } from './../Framework/QueryDefinition';
import { App } from "../Framework/App" 


export class SplashPage extends App {

     clientOnly() : boolean {
         return false;
     }

     getName() : string {
         return "SplashPage";
     }

     onInit () : void {

     }

     getUIQuery() : QueryDefinition {
        return new SplashPageAppQuery();
     }

     onInitialRender(parent_element : HTMLElement) : void {
        setTimeout( this.requestClose.bind(this),50000);
     }

     requestClose() {
        $(document).trigger("RequestClose", [this, this])
     }

     queryComplete(queryDef : QueryDefinition) : void {

     }

}

let func = function (global : any) {
    global.MagicMirror.addApplication(new SplashPage());
}
func(window);