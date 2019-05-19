
export class DeviceInfo {
    public id : string | undefined;
    public name : string | undefined;
    public width_value:number;
    public width_unit:string;
    public height_value:number;
    public height_unit:string;

    constructor(deviceCanvas:Document | string | object) {
        if(deviceCanvas instanceof Document) {
            this.width_value = deviceCanvas.documentElement.clientWidth;
            this.height_value = deviceCanvas.documentElement.clientHeight;
            this.width_unit = "px";
            this.height_unit = "px";
            return;
        } 
        let deviceDictionary : {id:string | undefined, width_value: number, height_value:number, width_unit:string, height_unit:string};
        if(typeof deviceCanvas === "string") {
            deviceDictionary = JSON.parse(deviceCanvas);
        } else {
            deviceDictionary = deviceCanvas as {width_value: number, height_value:number, width_unit:string, height_unit:string, id:string};
        }
        this.id = deviceDictionary.id;
        this.width_unit = deviceDictionary["width_unit"];
        this.width_value = deviceDictionary["width_value"];
        this.height_value = deviceDictionary["height_value"];
        this.height_unit = deviceDictionary["height_unit"];
    }

    public static CreateDeviceInfoFromJSON(data:{width_value: number, height_value:number, width_unit:string, height_unit:string}) {

    }

    private GetWidthCSSString () : string {
        return "width:" + this.GetWidthText() + ";";
      }
  
      private GetHeightCssString() : string{
          return "height:" + this.GetHeightText() + ";";
      }
  
      private GetWidthText() : string {
          return this.width_value + this.width_unit;
      }
  
      private GetHeightText() : string {
          return this.height_value + this.height_unit;
      }

    public TranslateToHTML() : HTMLElement {
        const inlineElement = document.createElement("style");
        inlineElement.innerText = ".mirrorContainer { " + 
                                        this.GetWidthCSSString() + 
                                        this.GetHeightCssString() +"} </style>"
        return inlineElement;
    }


}