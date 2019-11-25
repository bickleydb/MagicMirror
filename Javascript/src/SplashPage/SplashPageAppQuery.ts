
import { QueryDefinition } from "../Framework/QueryDefinition";

// tslint:disable-next-line: interface-name
export interface StatementUIQueryResult {
    htmlResponse: string;
}

export class SplashPageAppQuery extends QueryDefinition {

    constructor() {
        super("/splash");
    }

    public get URL(): string {
        return super.URL;
    }
}
