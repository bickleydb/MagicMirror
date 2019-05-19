import { QueryDefinition } from '../Framework/QueryDefinition';
import { App } from "../Framework/App" 


export class WeatherForcastApp extends App {


    private elementDict : { [id :string ] : JQuery};
    
    constructor() {
        super();
        this.elementDict = {};
    }

    clientOnly() : boolean {
        return false;
    }

    getName() : string {
        return "WeatherForcastApp";
    }

    onInit () : void {

    }

    getUIQuery() : QueryDefinition {
        return new QueryDefinition("/weather/forcastView");
    }

    onInitialRender(parent_element : HTMLElement) : void {

    }

    queryComplete(queryDef : QueryDefinition) : void {

    }

    cacheElements() : void {

    }
}

let func = function (global : any) {
    global.MagicMirror.addApplication(new WeatherForcastApp());
};
func(window);