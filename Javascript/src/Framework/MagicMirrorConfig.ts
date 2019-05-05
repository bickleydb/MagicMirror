export class MagicMirrorConfig {

    private numRows : number;
    private numColumns : number;

    constructor(queryResponse : {rows : number, columns : number, widthValue : number, widthUnit:string, heightValue:number, heightUnit:string}) { 
        this.numColumns = queryResponse.columns;
        this.numRows = queryResponse.rows;
    }

    public get NumRows() : number {
        return this.numRows;
    }

    public get NumColumns() : number {
        return this.numColumns;
    }

    public set NumRows(value:number)  {
        this.numRows = value;
    }

    public set NumColumns(value:number)  {
        this.numColumns = value;
    }

    public TranslateToHTML() : HTMLElement {
        const inlineElement = document.createElement("style");
        inlineElement.innerText = ".mirrorContainer { " +
                                    this.GetTemplateRowsCSSString() +
                                    this.GetTemplateColsCSSString() + 
                                    "} </style>"
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


  


}