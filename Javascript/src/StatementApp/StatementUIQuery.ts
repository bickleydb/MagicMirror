import { StatementUIQueryResult } from './StatementUIQuery';
import { QueryDefinition } from "../Framework/QueryDefinition";


export interface StatementUIQueryResult {
    htmlResponse : string
}


export class StatementUIQuery extends QueryDefinition {
    
    constructor() {
        super("/statements/");
    }

    public get URL() : string {
        return super.URL;
    }

    public GetResults() : StatementUIQueryResult {
        const responseVals = this.getResultVals();
        return {
            htmlResponse : responseVals.GetValue("htmlResponse")
        }
    }
}