export class AppUIConfig {

    private width:Number = 0;
    private height:Number = 0;
    
    private rowStart : number = 0;
    private rowEnd : number = 0;
    private columnStart : number = 0;
    private columnEnd : number = 0;

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

}