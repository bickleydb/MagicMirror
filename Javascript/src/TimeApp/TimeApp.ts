import { TimeAppQuery, TimeAppQueryResult } from './TimeAppQuery';
import {TimeAppUIQuery } from './TimeAppUIQuery';
import { App } from "../Framework/App" 

export class TimeApp extends App {


    private ElementIdSelectors = {
        hourFistDigit: "#hourFirstDigit",
        hourSecondDigit: "#hourSecondDigit",
        hourContainer: "#hourContainer",
        minuteFirstDigit: "#minuteFirstDigit",
        minuteSecondDigit: "#minuteSecondDigit",
        minuteContainer: "#minuteContainer",
        hourSeperator: "#hourSeperator",
        monthElement: "#monthElement",
        dayOfWeekElememt: "#dayOfWeekElement",
        dayOfMonthElement: "#dayOfMonthElement",
        yearElement: "#yearElement",
        timeDisplay: "#timeDisplay",
        dayOfWeekSeperator: "#dayOfWeekSeperator",
        dayOfMonthSeperator : "#dayOfMonthSeperator",
        dateDisplay: "#dateDisplay",
    }

    private HourFirstDigitValue : string = "";
    private HourSecondDigitValue: string = "";
    private MinuteFirstDigitValue : string = "";
    private MinuteSecondDigitValue : string = "";
    private MonthValue :string = "";
    private DayOfWeekValue: string = "";
    private DayOfMonthValue: string = "";
    private YearValue: string = "";
    
    private classes = {
        digit: "digit",
    };

    private updateLoopId = -1;
    private elementDict : { [id :string ] : HTMLElement};

    private ParentHTML : HTMLElement | null = null;

    constructor() {
        super();
        this.elementDict = {};
       
    }
    clientOnly() {
        return false;
    }

    getUIQuery() {
        return new TimeAppUIQuery();
    }

    onInit() {
    }

    getName() {
        return "timeApp";
    }

    onInitialRender(parentElement : HTMLElement) {
        this.ParentHTML = parentElement;
        this.updateUI();
        this.updateLoopId = setInterval(this.updateUI.bind(this), 10000);
    }

    updateUI() {
        const update = new TimeAppQuery();
        $(document).trigger("RequestQuery", [update, this]);
    }

    buildSingleDiv(elementID : string, ...classList : string[]) {
        let newElement = document.createElement("div");
        newElement.id = elementID;
        classList.forEach(className => {
            newElement.classList.add(className);
        });

        this.elementDict[elementID] = newElement;
        return newElement;
    }
    buildTwoDigitElement(firstDigitID : string, secondDigitID : string, containerID : string) {
        const parentElement = this.buildSingleDiv(containerID, this.classes.digit);
        const firstDigit = this.buildSingleDiv(firstDigitID, this.classes.digit);
        const secondDigit = this.buildSingleDiv(secondDigitID, this.classes.digit);
        parentElement.appendChild(firstDigit);
        parentElement.appendChild(secondDigit);
        return parentElement;
    }

    getParentElement() : HTMLElement { 
        if(this.ParentHTML === null) {
            return document.createElement("div");
        }
        return this.ParentHTML;
    }


    queryComplete(queryDef : TimeAppQuery) {
        const queryResults = queryDef.GetResults();
        const parentElement = this.getParentElement();

        if (queryResults.HourFirstDigit  != this.HourFirstDigitValue) {
            const hourFirstDigit = parentElement.querySelector(this.ElementIdSelectors.hourFistDigit);
            if(hourFirstDigit) {
                this.HourFirstDigitValue = queryResults.HourFirstDigit;
                hourFirstDigit.innerHTML = this.HourFirstDigitValue;
            }
        }

        if (queryResults.HourSecondDigit  != this.HourSecondDigitValue) {
            const hourSecondDigit = parentElement.querySelector(this.ElementIdSelectors.hourSecondDigit);
            if(hourSecondDigit) {
                this.HourSecondDigitValue = queryResults.HourSecondDigit;
                hourSecondDigit.innerHTML = this.HourFirstDigitValue;
            }
        }

        if (queryResults.MinuteFirstDigit  != this.MinuteFirstDigitValue) {
            const minuteFirstDigit = parentElement.querySelector(this.ElementIdSelectors.minuteFirstDigit);
            if(minuteFirstDigit) {
                this.MinuteFirstDigitValue = queryResults.MinuteFirstDigit;
                minuteFirstDigit.innerHTML = this.MinuteFirstDigitValue;
            }
        }

        if (queryResults.MinuteSecondDigit  != this.MinuteSecondDigitValue) {
            const minuteSecondDigit = parentElement.querySelector(this.ElementIdSelectors.minuteSecondDigit);
            if(minuteSecondDigit) {
                this.MinuteSecondDigitValue = queryResults.MinuteSecondDigit;
                minuteSecondDigit.innerHTML = this.MinuteSecondDigitValue;
            }
        }

        if (queryResults.DayOfWeek  != this.DayOfWeekValue) {
            const dayOfWeek = parentElement.querySelector(this.ElementIdSelectors.dayOfWeekElememt);
            if(dayOfWeek) {
                this.DayOfWeekValue = queryResults.DayOfWeek;
                dayOfWeek.innerHTML = this.DayOfWeekValue;
            }
        }

        if (queryResults.Month  != this.MonthValue) {
            const monthValue = parentElement.querySelector(this.ElementIdSelectors.monthElement);
            if(monthValue) {
                this.MonthValue = queryResults.Month;
                monthValue.innerHTML = this.MonthValue;
            }
        }

        if (queryResults.DayOfMonth  != this.DayOfMonthValue) {
            const dayOfMonthValue = parentElement.querySelector(this.ElementIdSelectors.dayOfMonthElement);
            if(dayOfMonthValue) {
                this.DayOfMonthValue = queryResults.DayOfMonth;
                dayOfMonthValue.innerHTML = this.DayOfMonthValue;
            }
        }

        if (queryResults.Year  != this.YearValue) {
            const yearElement = parentElement.querySelector(this.ElementIdSelectors.yearElement);
            if(yearElement) {
                this.YearValue = queryResults.Year;
                yearElement.innerHTML = this.YearValue;
            }
        }
    }
}

let func = function (global : any) {
    global.MagicMirror.addApplication(new TimeApp());
};
func(window);