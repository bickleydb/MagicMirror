import { TimeAppQuery, TimeAppData } from './TimeAppQuery';
import { TimeAppUIQuery } from './TimeAppUIQuery';
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
    private HasBeenUpdated : Boolean = false;
    private BackingData : TimeAppData;
    
    private classes = {
        digit: "digit",
    };

    private updateLoopId = -1;
    private elementDict : { [id :string ] : HTMLElement};

    private ParentHTML : HTMLElement | null = null;

    constructor() {
        super();
        this.elementDict = {};
        this.BackingData = this.createDefaultData();
       
    }

    createDefaultData() : TimeAppData {
        return {
            HourFirstDigit : "",
            HourSecondDigit: "",
            MinuteFirstDigit : "",
            MinuteSecondDigit : "",
            Month : "",
            DayOfWeek: "",
            DayOfMonth: "",
            Year: "",
            HourSeperator:"",
            DayOfWeekSeperator:""
        }
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
        this.updateLoopId = window.setInterval(this.updateUI.bind(this), 1000);
    }

    updateUI() {
        const update = new TimeAppQuery();
        $(document).trigger("RequestQuery", [update, this]);
    }

    getParentElement() : HTMLElement { 
        if(this.ParentHTML === null) {
            this.ParentHTML = document.createElement("div");
        }
        return this.ParentHTML;
    }

    digitUIUpdate(parentElement:HTMLElement, newValue:string, selector:string) : void {
        const digitElement : HTMLElement|null = parentElement.querySelector(selector);
        if(digitElement) {
            const newPercentage = (parseInt(newValue) * -10) + "%";
            $(digitElement).animate({top:newPercentage});
        }
    }

    updateUserInterface(queryResults:TimeAppData, parentElement:HTMLElement, forceUpdate:boolean=false) {
        if (queryResults.HourFirstDigit  != this.BackingData.HourFirstDigit || forceUpdate) {
            this.digitUIUpdate(parentElement, queryResults.HourFirstDigit,this.ElementIdSelectors.hourFistDigit);
        }

        if (queryResults.HourSecondDigit  != this.BackingData.HourSecondDigit || forceUpdate) {
            this.digitUIUpdate(parentElement, queryResults.HourSecondDigit,this.ElementIdSelectors.hourSecondDigit);
        }

        if (queryResults.MinuteFirstDigit  != this.BackingData.MinuteFirstDigit || forceUpdate) {
            this.digitUIUpdate(parentElement, queryResults.MinuteFirstDigit,this.ElementIdSelectors.minuteFirstDigit);
        }

        if (queryResults.MinuteSecondDigit  != this.BackingData.MinuteSecondDigit || forceUpdate) {
            this.digitUIUpdate(parentElement,queryResults.MinuteSecondDigit,this.ElementIdSelectors.minuteSecondDigit);
        }

        if (queryResults.DayOfWeek  != this.BackingData.DayOfWeek || forceUpdate) {
            const dayOfWeek = parentElement.querySelector(this.ElementIdSelectors.dayOfWeekElememt);
            if(dayOfWeek) {
                dayOfWeek.innerHTML = queryResults.DayOfWeek;
            }
        }

        if (queryResults.Month  != this.BackingData.Month || forceUpdate) {
            const monthValue = parentElement.querySelector(this.ElementIdSelectors.monthElement);
            if(monthValue) {
                monthValue.innerHTML = queryResults.Month;
            }
        }

        if (queryResults.DayOfMonth  != this.BackingData.DayOfMonth|| forceUpdate) {
            const dayOfMonthValue = parentElement.querySelector(this.ElementIdSelectors.dayOfMonthElement);
            if(dayOfMonthValue) {
                dayOfMonthValue.innerHTML = queryResults.DayOfMonth;
            }
        }

        if (queryResults.Year  != this.BackingData.Year|| forceUpdate) {
            const yearElement = parentElement.querySelector(this.ElementIdSelectors.yearElement);
            if(yearElement) {
                yearElement.innerHTML = queryResults.Year;
            }
        }
    }

    queryComplete(queryDef : TimeAppQuery) {
        const queryResults = queryDef.GetResults();
        this.updateUserInterface(queryResults,this.getParentElement(), !this.HasBeenUpdated)
        this.BackingData = queryResults;
        this.HasBeenUpdated = true;
    }
}

let func = function (global : any) {
    global.MagicMirror.addApplication(new TimeApp());
};
func(window);