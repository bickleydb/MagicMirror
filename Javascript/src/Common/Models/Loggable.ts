export interface Loggable {
    ToLoggableString() : string
}

class LoggableConsts {
    static readonly ObjectDelim = ",";
    static readonly ObjectProp = ";";
}


export abstract class ArrayLoggable implements Loggable {

    abstract GetLoggableValues : any[]

    ToLoggableString(): string {
        return "{".concat(
        this.GetLoggableValues.map( (value: Loggable|string|number, index: number ) => 
            {
                if(typeof value === "number") {
                    return value + "";
                } else if (typeof value == "string") {
                    return value;
                } else {
                    return value.ToLoggableString();
                }
            }).join(LoggableConsts.ObjectDelim)
        ).concat("}")
    }
}

export abstract class ObjectLoggable extends Object implements Loggable {
    ToLoggableString(): string {
        let resultStr = "";
        for(let property in this) {
            if(this.hasOwnProperty(property)) {
                resultStr = resultStr + ", " + property + ":" + this[property] + LoggableConsts.ObjectProp + ","; 
            }
        }
        return resultStr;
    }

}