import { TimeAppQuery } from './TimeAppQuery';
import { QueryDefinition } from './../Framework/QueryDefinition';
import { App } from "../Framework/App" 

export class TimeApp extends App {


    private elementIds = {
        hourFistDigit: "hourFirstDigit",
        hourSecondDigit: "hourSecondDigit",
        hourContainer: "hourContainer",
        minuteFirstDigit: "minuteFirstDigit",
        minuteSecondDigit: "minuteSecondDigit",
        minuteContainer: "minuteContainer",
        hourSeperator: "hourSeperator",
        monthElement: "monthElement",
        dayOfWeekElememt: "dayOfWeekElement",
        dayOfMonthElement: "dayOfMonthElement",
        yearElement: "yearElement",
        timeDisplay: "timeDisplay",
        dayOfWeekSeperator: "dayOfWeekSeperator",
        dateDisplay: "dateDisplay",
    }

    private Minute = -1;
    private Hour = -1;
    private Day = -1;
    private DayOfWeek = -1;
    private Month = "";
    private Year = -1;
    private HourSeperator = "";
    private MinuteSeperator = "";
    private DayOfWeekSeperator = "";
    
    private daysOfWeek = [
        "Monday", "Tuesday", "Wenesday", "Thursday", "Friday", "Saturday", "Sunday"
    ];

    private Months = [
        "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ];

    private classes = {
        digit: "digit",
    };

    private updateLoopId = -1;
    private elementDict : { [id :string ] : HTMLElement};



    constructor() {
        super();
        this.elementDict = {};
       
    }
    clientOnly() {
        return true;
    }
    getUIQuery() {
        return new TimeAppQuery();
    }
    onInit() {
    }
    getName() {
        return "timeApp";
    }

    onInitialRender(parentElement : HTMLElement) {
        parentElement.appendChild(this.buildTimeDisplayHTML());
        parentElement.appendChild(this.buildDateDisplayHTML());
        this.updateUI();
        this.updateLoopId = setInterval(this.updateUI.bind(this), 1000);
    }
    updateUI() {
        const update = new TimeAppQuery();
        const currentDate = new Date();
        QueryDefinition.SetResponseVals(update, { key: "Minute", value: currentDate.getMinutes() }, { key: "Hour", value: currentDate.getHours() }, { key: "Day", value: currentDate.getDate() }, { key: "DayOfWeek", value: this.daysOfWeek[currentDate.getDay()] }, { key: "Month", value: currentDate.getMonth() }, { key: "Year", value: currentDate.getFullYear() }, { key: "HourSeperator", value: ":" }, { key: "MinuteSeperator", value: ":" }, { key: "DayOfWeekSeperator", value: ",&nbsp" });
        this.queryComplete(update);
    }
    buildDateDisplayHTML() {
        const parentElement = this.buildSingleDiv(this.elementIds.dateDisplay);
        parentElement.appendChild(this.buildSingleDiv(this.elementIds.dayOfWeekElememt, this.classes.digit));
        parentElement.appendChild(this.buildSingleDiv(this.elementIds.dayOfWeekSeperator, this.classes.digit));
        parentElement.appendChild(this.buildSingleDiv(this.elementIds.monthElement, this.classes.digit));
        parentElement.appendChild(this.buildSingleDiv(this.elementIds.yearElement, this.classes.digit));
        return parentElement;
    }
    buildTimeDisplayHTML() {
        const parentElement = this.buildSingleDiv(this.elementIds.timeDisplay);
        const hourHTML = this.buildHourHTML();
        const minuteHTML = this.buildMinuteHTML();
        const seperatorHTML = this.buildSingleDiv(this.elementIds.hourSeperator, this.classes.digit);
        parentElement.appendChild(hourHTML);
        parentElement.appendChild(seperatorHTML);
        parentElement.appendChild(minuteHTML);
        return parentElement;
    }
    buildHourHTML() {
        return this.buildTwoDigitElement(this.elementIds.hourFistDigit, this.elementIds.hourSecondDigit, this.elementIds.hourContainer);
    }
    buildMinuteHTML() {
        return this.buildTwoDigitElement(this.elementIds.minuteFirstDigit, this.elementIds.minuteSecondDigit, this.elementIds.minuteContainer);
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

    queryComplete(queryDef : QueryDefinition) {
        const currentDate = new Date();
        QueryDefinition.SetResponseVals(queryDef, { Minute: currentDate.getMinutes(),
            Hour: currentDate.getHours(),
            Day: currentDate.getDate(),
            DayOfWeek: this.daysOfWeek[currentDate.getDay()],
            Month: currentDate.getMonth(),
            Year: currentDate.getFullYear(),
            HourSeperator: ":",
            MinuteSeperator: ":",
            DayOfWeekSeperator: ",&nbsp" });

        const queryResults = queryDef.GetResults();

        if (queryResults.Hour != this.Hour) {
            const displayVal = (queryResults.Hour > 12) ? queryResults.Hour - 12 : queryResults.Hour;
            this.elementDict[this.elementIds.hourFistDigit].innerText = displayVal >= 10 ? (displayVal + "").charAt(0) : " ";
            this.elementDict[this.elementIds.hourSecondDigit].innerText = displayVal % 10 + "";
            this.Hour = queryResults.Hour;
        }
        if (queryResults.Minute != this.Minute) {
            this.elementDict[this.elementIds.minuteFirstDigit].innerText = queryResults.Minute >= 10 ? (queryResults.Minute + "").charAt(0) : "0";
            this.elementDict[this.elementIds.minuteSecondDigit].innerText = queryResults.Minute % 10 + "";
            this.Minute = queryResults.Minute;
        }
        if (queryResults.HourSeperator != this.HourSeperator) {
            this.elementDict[this.elementIds.hourSeperator].innerText = queryResults.HourSeperator;
            this.HourSeperator = queryResults.HourSeperator;
        }
        if (queryResults.DayOfWeek != this.DayOfWeek) {
            this.elementDict[this.elementIds.dayOfWeekElememt].innerText = queryResults.DayOfWeek + "";
            this.DayOfWeek = queryResults.DayOfWeek;
        }
        if (queryResults.Month != this.Month) {
            this.elementDict[this.elementIds.monthElement].innerText = this.Months[Number(queryResults.Month)];
            this.Month = queryResults.Month;
        }
        if (queryResults.DayOfWeekSeperator != this.DayOfWeekSeperator) {
            this.elementDict[this.elementIds.dayOfWeekSeperator].innerText = queryResults.DayOfWeekSeperator;
            this.DayOfWeekSeperator = queryResults.DayOfWeekSeperator;
        }
        if (queryResults.Year != this.Year) {
            this.elementDict[this.elementIds.yearElement].innerText = queryResults.Year + "";
            this.Year = queryResults.Year;
        }
    }
}

let func = function (global : any) {
    global.MagicMirror.addApplication(new TimeApp());
};
func(window);