import { KeyValuePair, BooleanFunction } from './../CommonTypes';
import { KeyValueDictionary } from "../Common/KeyValueDictionary";

export class QueryDefinition {

    private static idNum: number = 0;

    private queryId: number;
    private url: string;
    private params: KeyValueDictionary;
    private returnVals: KeyValueDictionary;
    private owningAppKey: string | number = "";

    public static BuildQuery(url: string, ...passedParams: KeyValuePair[]): QueryDefinition {
        let query: QueryDefinition = new QueryDefinition(url);
        query.setupParameters(passedParams);
        return query;
    }

    public static SetParamVals(query:QueryDefinition, ...params:KeyValuePair[]) : void {
        params.forEach(element => {      
            query.params.Add(element.key, element.value);
        });
    }

    public static SetResponseVals(query: QueryDefinition, ...params: any[]): void {
        params.forEach(element => {
            for(let property in element) {
                query.returnVals.Add(property, element[property]);
            }
   
        });
    }

    constructor(url: string) {
        this.url = url;
        this.queryId = QueryDefinition.idNum;
        this.params = new KeyValueDictionary();
        this.returnVals = new KeyValueDictionary();
    }

    public GetResults() : any {}

    protected setupParameters(valuePairs: KeyValuePair[]): void {
        valuePairs.forEach(element => {
            this.params.Add(element.key, element.value);
        });
    }

    private static updateIdNum(): void {
        QueryDefinition.idNum++;
    }

    public get URL(): string {
        return this.url;
    }

    public getParams(): KeyValueDictionary {
        return this.params;
    }

    public getOwningAppKey(): string | number {
        return this.owningAppKey;
    }

    public setOwningAppKey(key: string | number): void {
        this.owningAppKey = key;
    }

    public getResultVals(): KeyValueDictionary {
        return this.returnVals;
    }
}

class RuleQuery extends QueryDefinition {

    private rule: BooleanFunction;

    constructor(url: string, rule: BooleanFunction, ...passedParams: KeyValuePair[]) {
        super(url)
        this.setupParameters(passedParams);
        this.rule = rule;
    }

    public evaluateRule(): boolean {
        return this.rule();
    }
}
