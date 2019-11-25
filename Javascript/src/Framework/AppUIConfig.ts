
// tslint:disable-next-line: interface-name
export interface AppConfigData {
    StartRow: number;
    EndRow: number;
    StartColumn: number;
    EndColumn: number;
    Priority: number;
}

export class AppUIConfig {

    public get Width() {
        return this.width;
    }

    public set Width(value: number) {
        this.width = value;
    }

    public get Height() {
        return this.height;
    }

    public set Height(value: number) {
        this.height = value;
    }

    public get RowStart() {
        return this.rowStart;
    }

    public set RowStart(value: number) {
        this.rowStart = value;
    }

    public get RowEnd() {
        return this.rowEnd;
    }
    public set RowEnd(value: number) {
        this.rowEnd = value;
    }

    public get ColumnStart() {
        return this.columnStart;
    }

    public set ColumnStart(value: number) {
        this.columnStart = value;
    }

    public get ColumnEnd() {
        return this.columnEnd;
    }

    public set ColumnEnd(value: number) {
        this.columnEnd = value;
    }

    public get LoadOnStart(): boolean {
        return this.loadOnStart;
    }

    public set LoadOnStart(value: boolean) {
        this.loadOnStart = value;
    }

    public static ParseFromObject(object: AppConfigData ): AppUIConfig {
        const appConfig = new AppUIConfig();
        appConfig.RowStart = object.StartRow;
        appConfig.RowEnd = object.EndRow;
        appConfig.ColumnStart = object.StartColumn;
        appConfig.ColumnEnd = object.EndColumn;
        appConfig.LoadOnStart = !!object.Priority;
        return appConfig;
    }

    private width: number = 0;
    private height: number = 0;

    private rowStart: number = 0;
    private rowEnd: number = 0;
    private columnStart: number = 0;
    private columnEnd: number = 0;

    private loadOnStart: boolean = false;

    public ApplyConfigToHTMLElement(element: any): void {
        this.ApplyGridStyles(element);
        this.ApplyRelativeSizeBaselineStyles(element);
    }

    private ApplyGridStyles(element: any): void {
        element.style.gridRowStart = this.RowStart;
        element.style.gridRowEnd = this.RowEnd;
        element.style.gridColumnStart = this.ColumnStart;
        element.style.gridColumnEnd = this.ColumnEnd;
    }

    private ApplyRelativeSizeBaselineStyles(element: HTMLElement) {
        element.style.position = "relative";
    }

}
