import {App} from "./App";

export class UIStack {

    private backingGrid : App[][][];

    constructor(gridRows: number, gridCols : number ) {
        this.backingGrid =[];
        for(var i = 0; i < gridRows; i++) {
            const gridRow = [];
            for(var t = 0; t < gridCols; t++) {
                gridRow.push([]);
            }
            this.backingGrid.push(gridRow);
        }
    }

    public PushApp(application : App, uiPosition : { RowStart : number, RowEnd:number, ColumnStart:number, ColumnEnd:number} ) : void {
        for(let rowIndex = uiPosition.RowStart-1; rowIndex < uiPosition.RowEnd-1; rowIndex++) {
            for(let colIndex = uiPosition.ColumnStart-1; colIndex < uiPosition.ColumnEnd-1; colIndex++) {
                const curStack = this.backingGrid[rowIndex][colIndex];
                this.backingGrid[rowIndex][colIndex].push(application);
            }
        }
    }

    public PopApp(application : App) : void {
        for(let rowIndex = 0; rowIndex < this.backingGrid.length; rowIndex++) {
            for(let colIndex = 0; colIndex < this.backingGrid[rowIndex].length; colIndex++) {
                const currentStack = this.backingGrid[rowIndex][colIndex];
                if(currentStack[currentStack.length-1] === application) {
                    currentStack.pop();
                }
            }
        }
    }

    public GetAppsToRender() : { [appName:string] : App } {
        const appList : {[key: string]: App} = {};
        const appsToIgnore : {[key: string]: App} = {};

        for(let rowIndex = 0; rowIndex < this.backingGrid.length; rowIndex++) {
            for(let colIndex = 0; colIndex < this.backingGrid[rowIndex].length; colIndex++) {
                const curStack = this.backingGrid[rowIndex][colIndex];
                if(curStack.length == 0) {continue;}
                let curApp = this.backingGrid[rowIndex][colIndex][curStack.length-1];
                if(!appList[curApp.getName()] && !appsToIgnore[curApp.getName()]) {
                    appList[curApp.getName()] = curApp;
                }
                for(let appStackIndex = curStack.length-2; appStackIndex >= 0; appStackIndex--) {
                    curApp = curStack[appStackIndex];
                    if(!appsToIgnore[curApp.getName()]) {
                        appsToIgnore[curApp.getName()] = curApp;
                        if(appList[curApp.getName()]) {
                            delete appList[curApp.getName()];
                        }
                    }
                }
            }
        }
        return appList;
    }

    








}