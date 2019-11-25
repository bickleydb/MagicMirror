import { Loggable } from "./Loggable";
import { LoggableConsts } from "./LoggableConstants";

export abstract class ObjectLoggable extends Object implements Loggable {
    public ToLoggableString(): string {
        let resultStr = "";
        for (const property in this) {
            if (this.hasOwnProperty(property)) {
                resultStr = resultStr + ", " + property + ":" + this[property] + LoggableConsts.ObjectProp + ",";
            }
        }
        return resultStr;
    }

}
