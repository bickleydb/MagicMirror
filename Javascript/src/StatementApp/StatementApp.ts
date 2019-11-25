import { App } from "../Framework/App";
import { QueryDefinition } from "./../Framework/QueryDefinition";
import { StatementAppQuery, StatementQueryResult } from "./StatementQuery";
import { StatementUIQuery } from "./StatementUIQuery";

export class StatementApp extends App {

    private static ElementIds = {
        message:     "message",
        sourceName : "source_title",
    };

    private elementDict: { [key: string]: HTMLElement };

    constructor() {
        super();
        this.elementDict = {};
    }

    public getName(): string {
        return "StatementApp";
    }

    public getUIQuery(): QueryDefinition {
        return new StatementUIQuery();
    }

    // tslint:disable-next-line: no-empty
    public onInit(): void { }

    public getReferenceToHTMLElement(parentElement: HTMLElement, elementId: string) {
        const htmlElement = parentElement.querySelector("#" + elementId) as HTMLElement;
        if (htmlElement) {
            this.elementDict[elementId] = htmlElement;
        }
    }

    public startUILoop(): void {
        this.updateUILoop();
        this.CreateTimer("UpdateStatement", 1000, this.updateUILoop.bind(this));
    }

    public updateUILoop(): void {
        const newQuery = new StatementAppQuery();
        $(document).trigger("RequestQuery", [newQuery, this]);
    }

    public onInitialRender(parentElement: HTMLElement): void {
        this.getReferenceToHTMLElement(parentElement, StatementApp.ElementIds.sourceName);
        this.getReferenceToHTMLElement(parentElement, StatementApp.ElementIds.message);
        this.startUILoop();
    }

    public queryComplete(queryDef: QueryDefinition): void {
        if (queryDef instanceof StatementAppQuery) {
            this.updateUI(queryDef.GetResults());
        }
    }

    public updateUI(result: StatementQueryResult): void {
        this.elementDict[StatementApp.ElementIds.sourceName].innerText = result.sourceName;
        this.elementDict[StatementApp.ElementIds.message].innerText = result.text;
    }

    public clientOnly(): boolean {
        return false;
    }
}

const func = (global: any) => {
    global.MagicMirror.addApplication(new StatementApp());
};
func(window);
