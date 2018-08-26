import { QueryDefinition } from './../Framework/QueryDefinition';
import { App } from "../Framework/App" 


export class WeatherApp extends App {


    private elementIds = {
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
        alert("test");

    }

    cacheElements() : void {
        this.elementDict[this.elementIds.currentTemp] = $("#"+this.elementIds.currentTemp);
        this.elementDict[this.elementIds.highTemp] = $("#"+this.elementIds.highTemp);
        this.elementDict[this.elementIds.lowTemp] = $("#"+this.elementIds.lowTemp);
        this.elementDict[this.elementIds.windSpeed] = $("#"+this.elementIds.windSpeed);
        this.elementDict[this.elementIds.labelCurrent] = $("#"+this.elementIds.labelCurrent);
        this.elementDict[this.elementIds.additionalValues] = $("#"+this.elementIds.additionalValues);
        this.elementDict[this.elementIds.sunStatusRow] = $("#"+this.elementIds.sunStatusRow);
        this.elementDict[this.elementIds.sunsetLabel] = $("#"+this.elementIds.sunsetLabel);
        this.elementDict[this.elementIds.sunsetTime] = $("#"+this.elementIds.sunsetTime);
        this.elementDict[this.elementIds.sunriseLabel] = $("#"+this.elementIds.sunriseLabel);
        this.elementDict[this.elementIds.sunriseTime] = $("#"+this.elementIds.sunriseTime);
        this.elementDict[this.elementIds.percipitationRow] = $("#"+this.elementIds.percipitationRow);
        this.elementDict[this.elementIds.humidityLabel] = $("#"+this.elementIds.humidityLabel);
        this.elementDict[this.elementIds.humidityValue] = $("#"+this.elementIds.humidityValue);
        this.elementDict[this.elementIds.snowLabel] = $("#"+this.elementIds.snowLabel);
        this.elementDict[this.elementIds.snowAmount] = $("#"+this.elementIds.snowAmount);
    }

}

let func = function (global : any) {
    global.MagicMirror.addApplication(new WeatherApp());
};
func(window);