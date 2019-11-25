import { App } from "../Framework/App";
import { QueryDefinition } from "./../Framework/QueryDefinition";

export class WeatherApp extends App {
    private elementIds: { [vals: string]: string } = {
        additionalValues : "additionalValues",
        currentTemp : "currentTemp",
        highTemp : "highTemp",
        humidityLabel : "humidityLabel",
        humidityValue : "humidityValue",
        labelCurrent : "labelCurrent",
        lowTemp : "lowTemp",
        percipitationRow : "percipitationRow",
        snowAmount : "snowAmount",
        snowLabel : "snowLabel",
        sunriseLabel : "sunriseLabel",
        sunriseTime : "sunriseTime",
        sunsetLabel : "sunsetLabel",
        sunsetTime : "sunsetTime",
        sunstatusRow : "sunStatusRow",
    };

    private elementDict: { [id: string ]: JQuery};

    constructor() {
        super();
        this.elementDict = {};
    }

    public clientOnly(): boolean {
        return false;
    }

    public getName(): string {
        return "WeatherApp";
    }

    // tslint:disable-next-line: no-empty
    public onInit(): void {}

    public getUIQuery(): QueryDefinition {
        return new QueryDefinition("/weather/");
    }

    public onInitialRender(parentElement: HTMLElement): void {
        this.cacheElements();
        this.CreateTimer("UpdateWeather", 10000, () => {this.onUIUpdate(); });
    }

    // tslint:disable-next-line: no-empty
    public onUIUpdate(): void { }

    // tslint:disable-next-line: no-empty
    public queryComplete(queryDef: QueryDefinition): void { }

    public cacheElements(): void {
        for (const prop in this.elementIds) {
            if (!this.elementIds.hasOwnProperty(prop)) {continue; }
            this.elementDict[(this.elementIds[prop] + "")] = $("#" + prop);
        }
    }
}

const func = (global: any) => {
    global.MagicMirror.addApplication(new WeatherApp());
};
func(window);
