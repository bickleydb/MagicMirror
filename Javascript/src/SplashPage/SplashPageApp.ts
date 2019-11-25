import { App } from "../Framework/App";
import { QueryDefinition } from "./../Framework/QueryDefinition";
import { SplashPageAppQuery } from "./SplashPageAppQuery";

export class SplashPage extends App {

     public clientOnly(): boolean {
         return false;
     }

     public getName(): string {
         return "SplashPage";
     }

     // tslint:disable-next-line: no-empty
     public onInit(): void { }

     public getUIQuery(): QueryDefinition {
        return new SplashPageAppQuery();
     }

     public onInitialRender(parentElement: HTMLElement): void {
        this.CreateTimer("CloseSplashScreen", 50000, this.requestClose.bind(this));
     }

     public requestClose() {
        $(document).trigger("RequestClose", [this, this]);
     }

     // tslint:disable-next-line: no-empty
     public queryComplete(queryDef: QueryDefinition): void { }

}

const func = (global: any) => {
    global.MagicMirror.addApplication(new SplashPage());
};
func(window);
