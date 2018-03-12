export interface KeyValuePair {
    key: any;
    value: any;
}

export interface BooleanFunction {
    (param?: any, ...params: (any | undefined)[]): boolean;
}
