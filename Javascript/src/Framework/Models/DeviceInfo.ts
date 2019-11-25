
// tslint:disable-next-line: interface-name
export interface DeviceInfoData {
    id: string | undefined;
    width_value: number;
    height_value: number;
    width_unit: string;
    height_unit: string;
}

export class DeviceInfo {

    public id: string | undefined;
    public name: string | undefined;
    public widthValue: number;
    public widthUnit: string;
    public heightValue: number;
    public heightUnit: string;

    constructor(deviceCanvas: Document | string | object) {
        if (deviceCanvas instanceof Document) {
            this.widthValue = deviceCanvas.documentElement.clientWidth;
            this.heightValue = deviceCanvas.documentElement.clientHeight;
            this.widthUnit = "px";
            this.heightUnit = "px";
            return;
        }
        let deviceDictionary: DeviceInfoData;
        if (typeof deviceCanvas === "string") {
            deviceDictionary = JSON.parse(deviceCanvas);
        } else {
            deviceDictionary = deviceCanvas as DeviceInfoData;
        }
        this.id = deviceDictionary.id;
        this.widthUnit = deviceDictionary.width_unit;
        this.widthValue = deviceDictionary.width_value;
        this.heightValue = deviceDictionary.height_value;
        this.heightUnit = deviceDictionary.height_unit;
    }

    public TranslateToHTML(): HTMLElement {
        const inlineElement = document.createElement("style");
        inlineElement.innerText = ".mirrorContainer { " +
                                        this.GetWidthCSSString() +
                                        this.GetHeightCssString() + "} </style>";
        return inlineElement;
    }

    private GetWidthCSSString(): string {
        return "width:" + this.GetWidthText() + ";";
      }

      private GetHeightCssString(): string {
          return "height:" + this.GetHeightText() + ";";
      }

      private GetWidthText(): string {
          return this.widthValue + this.widthUnit;
      }

      private GetHeightText(): string {
          return this.heightValue + this.heightUnit;
      }

}
