import { QueryDefinition } from './../Framework/QueryDefinition';
import { App } from "../Framework/App" 


export class WeatherApp extends App {


    private elementIds : { [vals : string] : string } = {
        currentTemp : "currentTemp",
        highTemp : "highTemp",
        lowTemp : "lowTemp",
        windSpeed : "windSpeed",
        labelCurrent : "labelCurrent",
        additionalValues : "additionalValues",
        sunStatusRow : "sunStatusRow",
        sunsetLabel : "sunsetLabel",
        sunsetTime : "sunsetTime", 
        sunriseLabel : "sunriseLabel",
        sunriseTime : "sunriseTime",
        percipitationRow : "percipitationRow",
        humidityLabel : "humidityLabel",
        humidityValue : "humidityValue",
        snowLabel : "snowLabel",
        snowAmount : "snowAmount",
    }

    private elementDict : { [id :string ] : JQuery};
    
    constructor() {
        super();
        this.elementDict = {};
    }

    clientOnly() : boolean {
        return false;
    }

    getName() : string {
        return "WeatherApp";
    }

    onInit () : void {

    }

    getUIQuery() : QueryDefinition {
        return new QueryDefinition("http://127.0.0.1:8000/weather/");
    }

    onInitialRender(parent_element : HTMLElement) : void {
        this.cacheElements();
    }

    queryComplete(queryDef : QueryDefinition) : void {
    }

    cacheElements() : void {
        for(let prop in this.elementIds) {
            if(!this.elementIds.hasOwnProperty(prop)) {continue;}
            this.elementDict[(this.elementIds[prop]+"")] = $("#"+prop);
        }
    }
}

let func = function (global : any) {
    global.MagicMirror.addApplication(new WeatherApp());
};
func(window);