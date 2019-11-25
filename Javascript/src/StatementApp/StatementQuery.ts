import { QueryDefinition } from "../Framework/QueryDefinition";

// tslint:disable-next-line: interface-name
export interface StatementQueryResult {
    sourceName: string;
    text: string;
}

export class StatementAppQuery extends QueryDefinition {
    private static URL_STRING: "/statements/getValue/";

        constructor() {
            super("/statements/getValue/");
        }

        public get URL(): string {
            return super.URL;
        }

        public GetResults(): StatementQueryResult {
            const responseVals = this.getResultVals();
            return {
                sourceName : responseVals.GetValue("sourceName"),
                text : responseVals.GetValue("text"),
            };
        }
}
