import { KeyValueDictionary } from "../Common/KeyValueDictionary";
import { BooleanFunction, KeyValuePair } from "./../CommonTypes";

export class QueryDefinition {

    public get URL(): string {
        return this.url;
    }

    public static BuildQuery(url: string, ...passedParams: KeyValuePair[]): QueryDefinition {
        const query: QueryDefinition = new QueryDefinition(url);
        query.setupParameters(passedParams);
        return query;
    }

    public static SetParamVals(query: QueryDefinition, ...params: KeyValuePair[]): void {
        params.forEach((element) => {
            query.params.Add(element.key, element.value);
        });
    }

    public static SetResponseVals(query: QueryDefinition, ...params: any[]): void {
        params.forEach((element) => {
            for (const property in element) {
                if ( !element.hasOwnProperty(property)) {continue; }
                query.returnVals.Add(property, element[property]);
            }

        });
    }

    private static idNum: number = 0;

    private static updateIdNum(): void {
        QueryDefinition.idNum++;
    }

    private url: string;
    private params: KeyValueDictionary;
    private returnVals: KeyValueDictionary;
    private owningAppKey: string | number = "";

    constructor(url: string) {
        this.url = url;
        this.params = new KeyValueDictionary();
        this.returnVals = new KeyValueDictionary();
    }

    // tslint:disable-next-line: no-empty
    public GetResults(): any {}

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

    protected setupParameters(valuePairs: KeyValuePair[]): void {
        valuePairs.forEach((element) => {
            this.params.Add(element.key, element.value);
        });
    }
}
