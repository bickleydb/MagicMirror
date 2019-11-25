import { App } from "../Framework/App";
import { TimeAppData, TimeAppQuery } from "./TimeAppQuery";
import { TimeAppUIQuery } from "./TimeAppUIQuery";

export class TimeApp extends App {

    private ElementIdSelectors = {
        dateDisplay: "#dateDisplay",
        dayOfMonthElement: "#dayOfMonthElement",
        dayOfMonthSeperator : "#dayOfMonthSeperator",
        dayOfWeekElememt: "#dayOfWeekElement",
        dayOfWeekSeperator: "#dayOfWeekSeperator",
        hourContainer: "#hourContainer",
        hourFistDigit: "#hourFirstDigit",
        hourSecondDigit: "#hourSecondDigit",
        hourSeperator: "#hourSeperator",
        minuteContainer: "#minuteContainer",
        minuteFirstDigit: "#minuteFirstDigit",
        minuteSecondDigit: "#minuteSecondDigit",
        monthElement: "#monthElement",
        timeDisplay: "#timeDisplay",
        yearElement: "#yearElement",
    };

    private HasBeenUpdated: boolean = false;
    private BackingData: TimeAppData;
    private ParentHTML: HTMLElement | null = null;

    constructor() {
        super();
        this.BackingData = this.createDefaultData();

    }

    public createDefaultData(): TimeAppData {
        return {
            DayOfMonth: "",
            DayOfWeek: "",
            DayOfWeekSeperator: "",
            HourFirstDigit : "",
            HourSecondDigit: "",
            HourSeperator: "",
            MinuteFirstDigit : "",
            MinuteSecondDigit : "",
            Month : "",
            Year: "",
        };
    }

    public clientOnly() {
        return false;
    }

    public getUIQuery() {
        return new TimeAppUIQuery();
    }

    // tslint:disable-next-line: no-empty
    public onInit() { }

    public getName() {
        return "timeApp";
    }

    public onInitialRender(parentElement: HTMLElement) {
        this.ParentHTML = parentElement;
        this.updateUI();
        this.CreateTimer("TimeUpdate", 1000, this.updateUI.bind(this));
    }

    public updateUI() {
        const update = new TimeAppQuery();
        $(document).trigger("RequestQuery", [update, this]);
    }

    public getParentElement(): HTMLElement {
        if (this.ParentHTML === null) {
            this.ParentHTML = document.createElement("div");
        }
        return this.ParentHTML;
    }

    public digitUIUpdate(parentElement: HTMLElement, newValue: string, selector: string): void {
        const digitElement: HTMLElement|null = parentElement.querySelector(selector);
        if (digitElement) {
            const newPercentage = (parseInt(newValue, 10) * -10) + "%";
            $(digitElement).animate({top: newPercentage});
        }
    }

    public updateUserInterface(queryResults: TimeAppData, parentElement: HTMLElement, forceUpdate: boolean= false) {
        if (queryResults.HourFirstDigit  !== this.BackingData.HourFirstDigit || forceUpdate) {
            this.digitUIUpdate(parentElement, queryResults.HourFirstDigit, this.ElementIdSelectors.hourFistDigit);
        }

        if (queryResults.HourSecondDigit  !== this.BackingData.HourSecondDigit || forceUpdate) {
            this.digitUIUpdate(parentElement, queryResults.HourSecondDigit, this.ElementIdSelectors.hourSecondDigit);
        }

        if (queryResults.MinuteFirstDigit  !== this.BackingData.MinuteFirstDigit || forceUpdate) {
            this.digitUIUpdate(parentElement, queryResults.MinuteFirstDigit, this.ElementIdSelectors.minuteFirstDigit);
        }

        if (queryResults.MinuteSecondDigit  !== this.BackingData.MinuteSecondDigit || forceUpdate) {
            this.digitUIUpdate(parentElement,
                 queryResults.MinuteSecondDigit,
                 this.ElementIdSelectors.minuteSecondDigit);
        }

        if (queryResults.DayOfWeek  !== this.BackingData.DayOfWeek || forceUpdate) {
            const dayOfWeek = parentElement.querySelector(this.ElementIdSelectors.dayOfWeekElememt);
            if (dayOfWeek) {
                dayOfWeek.innerHTML = queryResults.DayOfWeek;
            }
        }

        if (queryResults.Month  !== this.BackingData.Month || forceUpdate) {
            const monthValue = parentElement.querySelector(this.ElementIdSelectors.monthElement);
            if (monthValue) {
                monthValue.innerHTML = queryResults.Month;
            }
        }

        if (queryResults.DayOfMonth  !== this.BackingData.DayOfMonth || forceUpdate) {
            const dayOfMonthValue = parentElement.querySelector(this.ElementIdSelectors.dayOfMonthElement);
            if (dayOfMonthValue) {
                dayOfMonthValue.innerHTML = queryResults.DayOfMonth;
            }
        }

        if (queryResults.Year  !== this.BackingData.Year || forceUpdate) {
            const yearElement = parentElement.querySelector(this.ElementIdSelectors.yearElement);
            if (yearElement) {
                yearElement.innerHTML = queryResults.Year;
            }
        }
    }

    public queryComplete(queryDef: TimeAppQuery) {
        const queryResults = queryDef.GetResults();
        this.updateUserInterface(queryResults, this.getParentElement(), !this.HasBeenUpdated);
        this.BackingData = queryResults;
        this.HasBeenUpdated = true;
    }
}

const func = (global: any) => { global.MagicMirror.addApplication(new TimeApp()); };
func(window);
