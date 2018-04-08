import { QueryDefinition } from './../Framework/QueryDefinition';
import { App } from "../Framework/App" 

export class TimeAppQuery extends QueryDefinition {

    private static URL_STRING = "";


    constructor() {
        super(TimeAppQuery.URL_STRING);
    }

    GetResults() {
        const results = this.getResultVals();
        return {
            Minute: results.GetValue("Minute"),
            Hour: results.GetValue("Hour"),
            Day: results.GetValue("Day"),
            DayOfWeek: results.GetValue("DayOfWeek"),
            Month: results.GetValue("Month"),
            Year: results.GetValue("Year"),
            HourSeperator: ":",
            MinuteSeperator: ":",
            DayOfWeekSeperator: ",",
        };
    }
}