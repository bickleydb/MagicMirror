import { LoggableConsts } from "./LoggableConstants";

// tslint:disable-next-line: interface-name
export interface Loggable {
    ToLoggableString(): string;
}

export abstract class ArrayLoggable implements Loggable {

    public abstract GetLoggableValues: any[];

    public ToLoggableString(): string {
        return "{".concat(
        this.GetLoggableValues.map( (value: Loggable|string|number, index: number ) => {
                if (typeof value === "number") {
                    return value + "";
                } else if (typeof value === "string") {
                    return value;
                } else {
                    return value.ToLoggableString();
                }
            }).join(LoggableConsts.ObjectDelim),
        ).concat("}");
    }
}


