import { StatementUIQuery } from './StatementUIQuery';
import { EventManager } from './../Common/EventManager';
import { StatementAppQuery, StatementQueryResult } from './StatementQuery';
import { KeyValuePair } from './../CommonTypes';
import { QueryDefinition } from './../Framework/QueryDefinition';
import { App } from "../Framework/App" 



export class StatementApp extends App {

    element_ids = {
        sourceName : "source_title",
        message:     "message"
    }

    private baseHTMLElement : null;

    private elementDict : { [key : string] : HTMLElement }


    private updateDBTimerId = -1;
    private updateUITimerId = -1;

    constructor() {
        super();
        this.elementDict = {};
    }


    getName() : string {
        return "StatementApp";
    }

    getUIQuery() : QueryDefinition {
        return new StatementUIQuery();
    }

    onInit () : void {

    }

    getReferenceToHTMLElement(parentElement : HTMLElement, elementId : string) {
        const htmlElement = parentElement.querySelector("#"+elementId) as HTMLElement;
        if(htmlElement) {
            this.elementDict[elementId] = htmlElement;
        }
    }

    startUILoop() : void {
        this.updateUITimerId = setInterval(this.updateUILoop.bind(this), 1000);
    }

    updateUILoop() : void {
        const newQuery = new StatementAppQuery();
        $(document).trigger("RequestQuery", [newQuery, this]);
    }

 
    onInitialRender(parentElement : HTMLElement) : void {
        this.getReferenceToHTMLElement(parentElement, this.element_ids.sourceName);
        this.getReferenceToHTMLElement(parentElement, this.element_ids.message);
        this.startUILoop();
    }

    queryComplete(queryDef : QueryDefinition) : void {
        if(queryDef instanceof StatementUIQuery) {
            

        } else if (queryDef instanceof StatementAppQuery) {
            this.updateUI(queryDef.GetResults());
        }
    }

    updateUI( result: StatementQueryResult) : void {
        this.elementDict[this.element_ids.sourceName].innerText = result.sourceName;
        this.elementDict[this.element_ids.message].innerText = result.text;
    }

    clientOnly() : boolean {
        return false;
    }
}

let func = function (global : any) {
    global.MagicMirror.addApplication(new StatementApp());
}
func(window);