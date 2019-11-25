import { QueryDefinition } from "../Framework/QueryDefinition";
import { StatementUIQueryResult } from "./StatementUIQuery";

// tslint:disable-next-line: interface-name
export interface StatementUIQueryResult {
    htmlResponse: string;
}

export class StatementUIQuery extends QueryDefinition {

    constructor() {
        super("/statements/");
    }

    public get URL(): string {
        return super.URL;
    }

    public GetResults(): StatementUIQueryResult {
        const responseVals = this.getResultVals();
        return {
            htmlResponse : responseVals.GetValue("htmlResponse"),
        };
    }
}
