export class MagicMirrorConfig {

    constructor(queryResponse : {rows : number, columns : number, widthValue : number, widthUnit:string, heightValue:number, heightUnit:string}) { 
        this.numColumns = queryResponse.columns;
        this.numRows = queryResponse.rows;
        this.widthValue = queryResponse.widthValue;
        this.widthUnit = queryResponse.widthUnit;
        this.heightValue = queryResponse.heightValue;
        this.heightUnit = queryResponse.heightUnit;
        

    }


    private numRows : number;
    private numColumns : number;
    private widthValue : number;
    private widthUnit : string;
    private heightValue : number;
    private heightUnit : string;




    public get NumRows() : number {
        return this.numRows;
    }

    public get NumColumns() : number {
        return this.numColumns;
    }

    public get WidthValue() : number {
        return this.widthValue;
    }

    public get WidthUnit() : string {
        return this.widthUnit;
    }

    public get HeightValue() : number {
        return this.heightValue;
    }

    public get HeightUnit() : string {
        return this.heightUnit;
    }

    public set NumRows(value:number)  {
        this.numRows = value;
    }

    public set NumColumns(value:number)  {
        this.numColumns = value;
    }

    public set WidthValue(value:number)  {
        this.widthValue = value;
    }

    public set WidthUnit(value:string)  {
        this.widthUnit = value;
    }

    public set HeightValue(value:number)  {
        this.heightValue = value;
    }

    public set HeightUnit(value:string)  {
        this.heightUnit = value;
    }

    public TranslateToHTML() : HTMLElement {
        const inlineElement = document.createElement("style");
        inlineElement.innerText = ".mirrorContainer { " + this.GetWidthCSSString() + 
                                                          this.GetHeightCssString() +
                                                          this.GetTemplateRowsCSSString() +
                                                          this.GetTemplateColsCSSString() + "} </style>"
        return inlineElement;
    }

    private GetTemplateColsCSSString() : string {
        return "grid-template-columns:" + this.GetTemplateValueString(this.NumColumns) + ";"
    }

    private GetTemplateRowsCSSString() : string {
        return "grid-template-rows:" + this.GetTemplateValueString(this.NumRows) + ";";
    }

    private GetTemplateValueString(value:number) : string {
        return ((100/value)+"% ").repeat(value); 
    }


    private GetWidthCSSString () : string {
      return "width:" + this.GetWidthText() + ";";
    }

    private GetHeightCssString() : string{
        return "height:" + this.GetHeightText() + ";";
    }

    private GetWidthText() : string {
        return this.WidthValue + this.WidthUnit;
    }

    private GetHeightText() : string {
        return this.HeightValue + this.HeightUnit;
    }


}