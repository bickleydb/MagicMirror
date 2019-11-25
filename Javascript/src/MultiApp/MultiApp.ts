import {App} from "../Framework/App";
import { ApplicationEventEnum, ApplicationRequestEnum } from "../Framework/AppEventsEnum";
import { QueryDefinition } from "../Framework/QueryDefinition";

export class MultiApp extends App {

    private ChildApps: App[] | null = null;

     public clientOnly(): boolean {
         return false;
     }

     public getName(): string {
         return "MultiApp";
     }

     public onInit(): void {
        return;
     }

     public getUIQuery(): QueryDefinition {
        return new QueryDefinition("");
     }

     // tslint:disable-next-line: no-empty
     public onInitialRender(parentElement: HTMLElement): void { }

     // tslint:disable-next-line: no-empty
     public queryComplete(queryDef: QueryDefinition): void { }

}
