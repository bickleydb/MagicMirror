import { App } from "../Framework/App" ;
import { QueryDefinition } from "./../Framework/QueryDefinition";

// tslint:disable-next-line: interface-name
export interface TimeAppData {
    HourFirstDigit: string;
    HourSecondDigit: string;
    HourSeperator: string;
    MinuteFirstDigit: string;
    MinuteSecondDigit: string;
    DayOfWeek: string;
    DayOfWeekSeperator: string;
    Month: string;
    DayOfMonth: string;
    Year: string;
}

export class TimeAppQuery extends QueryDefinition {

    private static URL_STRING = "/time/getTime";

    constructor() {
        super(TimeAppQuery.URL_STRING);
    }

    public SetResult(preDeterminedResult: TimeAppData): void {
        QueryDefinition.SetResponseVals(this, preDeterminedResult);
    }

    public GetResults(): TimeAppData {
        const results = this.getResultVals();
        return {
            DayOfMonth: results.GetValue("dayOfMonth"),
            DayOfWeek: results.GetValue("dayOfWeek"),
            DayOfWeekSeperator: results.GetValue("dayOfWeekSeperator"),
            HourFirstDigit: results.GetValue("hourFirstDigit"),
            HourSecondDigit: results.GetValue("hourSecondDigit"),
            HourSeperator: results.GetValue("hourSeperator"),
            MinuteFirstDigit: results.GetValue("minuteFirstDigit"),
            MinuteSecondDigit: results.GetValue("minuteSecondDigit"),
            Month: results.GetValue("month"),
            Year: results.GetValue("year"),
        };
    }
}
