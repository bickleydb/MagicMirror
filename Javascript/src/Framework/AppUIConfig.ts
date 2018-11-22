
export class AppUIConfig {

    private width:Number = 0;
    private height:Number = 0;
    
    private rowStart : number = 0;
    private rowEnd : number = 0;
    private columnStart : number = 0;
    private columnEnd : number = 0;

    private loadOnStart : boolean = false;

    public get Width() {
        return this.width;
    }

    public get Height() {
        return this.height;
    }

    public set Width(value:Number) {
        this.width=value;
    }

    public set Height(value:Number) {
        this.height=value;
    }

    public get RowStart() {
        return this.rowStart;
    }

    public get RowEnd() {
        return this.rowEnd;
    }
    public get ColumnStart() {
        return this.columnStart;
    }

    public get ColumnEnd() {
        return this.columnEnd;
    }
    
    public get LoadOnStart() : boolean {
        return this.loadOnStart;
    }

    public set LoadOnStart(value : boolean) {
        this.loadOnStart = value;
    }

    public set RowStart(value : number) {
        this.rowStart = value;
    }

    public set RowEnd(value : number) {
        this.rowEnd = value;
    }
    public set ColumnStart(value : number) {
        this.columnStart = value;
    }

    public set ColumnEnd(value : number) {
        this.columnEnd = value;
    }

    public static ParseFromObject (object : {StartRow:number, EndRow:number, StartColumn:number, EndColumn:number, Priority:number} ) : AppUIConfig {
        const appConfig = new AppUIConfig();
        appConfig.RowStart = object.StartRow;
        appConfig.RowEnd = object.EndRow;
        appConfig.ColumnStart = object.StartColumn;
        appConfig.ColumnEnd = object.EndColumn;
        appConfig.LoadOnStart = !!object.Priority;
        return appConfig;
    }

    private ApplyGridStyles(element : any) : void {
        element.style.gridRowStart = this.RowStart;
        element.style.gridRowEnd = this.RowEnd;
        element.style.gridColumnStart = this.ColumnStart;
        element.style.gridColumnEnd = this.ColumnEnd;
    }

    private ApplyRelativeSizeBaselineStyles(element : HTMLElement) {
        element.style.position = "relative";
    }

    public ApplyConfigToHTMLElement(element : any) : void {
        this.ApplyGridStyles(element);
        this.ApplyRelativeSizeBaselineStyles(element);
    }

}