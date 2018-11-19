import { QueryDefinition } from './../Framework/QueryDefinition';
import { App } from "../Framework/App" 

export interface TimeAppQueryResult {
    HourFirstDigit: string,
    HourSecondDigit: string,
    HourSeperator: string,
    MinuteFirstDigit: string,
    MinuteSecondDigit: string,
    DayOfWeek: string,
    DayOfWeekSeperator: string,
    Month: string,
    DayOfMonth: string,
    Year: string
    
}

export class TimeAppQuery extends QueryDefinition {

    private static URL_STRING = "http://127.0.0.1:8000/time/getTime";


    constructor() {
        super(TimeAppQuery.URL_STRING);
    }

    GetResults() : TimeAppQueryResult {
        const results = this.getResultVals();
        return {
            HourFirstDigit: results.GetValue("hourFirstDigit"),
            HourSecondDigit: results.GetValue("hourSecondDigit"),
            HourSeperator: results.GetValue("hourSeperator"),
            MinuteFirstDigit: results.GetValue("minuteFirstDigit"),
            MinuteSecondDigit: results.GetValue("minuteSecondDigit"),
            DayOfWeek: results.GetValue("dayOfWeek"),
            DayOfWeekSeperator: results.GetValue("dayOfWeekSeperator"),
            Month: results.GetValue("month"),
            DayOfMonth: results.GetValue("dayOfMonth"),
            Year: results.GetValue("year")
        };
    }
}