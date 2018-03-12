export class AppUIConfig {

    private width:Number = 0;
    private height:Number = 0;

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
}