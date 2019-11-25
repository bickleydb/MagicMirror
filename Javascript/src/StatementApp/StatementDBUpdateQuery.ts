import { QueryDefinition } from "../Framework/QueryDefinition";

export class StatementAppQuery extends QueryDefinition {
    private static URL_STRING: "/statements/updateDB/";

        constructor() {
            super(StatementAppQuery.URL_STRING);
        }
}
