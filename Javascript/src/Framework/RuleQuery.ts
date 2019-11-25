import { BooleanFunction, KeyValuePair } from "../CommonTypes";
import { QueryDefinition } from "./QueryDefinition";

class RuleQuery extends QueryDefinition {

    private rule: BooleanFunction;

    constructor(url: string, rule: BooleanFunction, ...passedParams: KeyValuePair[]) {
        super(url);
        this.setupParameters(passedParams);
        this.rule = rule;
    }

    public evaluateRule(): boolean {
        return this.rule();
    }
}
