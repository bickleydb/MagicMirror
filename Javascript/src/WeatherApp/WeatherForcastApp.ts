import { App } from "../Framework/App";
import { QueryDefinition } from "../Framework/QueryDefinition";

export class WeatherForcastApp extends App {

    private elementDict: { [id: string ]: JQuery};

    constructor() {
        super();
        this.elementDict = {};
    }

    public clientOnly(): boolean {
        return false;
    }

    public getName(): string {
        return "WeatherForcastApp";
    }

    // tslint:disable-next-line: no-empty
    public onInit(): void { }

    public getUIQuery(): QueryDefinition {
        return new QueryDefinition("/weather/forcastView");
    }

    // tslint:disable-next-line: no-empty
    public onInitialRender(parentElement: HTMLElement): void { }

    // tslint:disable-next-line: no-empty
    public queryComplete(queryDef: QueryDefinition): void { }

    // tslint:disable-next-line: no-empty
    public cacheElements(): void { }
}

const func = (global: any) => {
    global.MagicMirror.addApplication(new WeatherForcastApp());
};
func(window);
