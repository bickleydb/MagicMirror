
import { QueryDefinition } from "../Framework/QueryDefinition";


export interface StatementUIQueryResult {
    htmlResponse : string
}


export class SplashPageAppQuery extends QueryDefinition {
    
    constructor() {
        super("/splash");
    }

    public get URL() : string {
        return super.URL;
    }
}