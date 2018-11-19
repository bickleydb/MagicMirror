import { TimeAppQuery } from './TimeAppQuery';
import { QueryDefinition } from "../Framework/QueryDefinition";

export interface TimeAppUIQueryResult {
    htmlResponse : string
}


export class TimeAppUIQuery extends QueryDefinition {
    
    constructor() {
        super("/time/index");
    }

    public get URL() : string {
        return super.URL;
    }

    public GetResults() : TimeAppUIQueryResult {
        const responseVals = this.getResultVals();
        return {
            htmlResponse : responseVals.GetValue("htmlResponse")
        }
    }
}