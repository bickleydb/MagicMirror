export interface PersistentSettings {
    magicMirrorDeviceId : string | undefined
    [key:string] : string | undefined
}

export class PersistentSettingsLoader {
    
    static readonly CookiePartDelim = ",";
    static readonly CookieValueDelim = "=";

    public LoadSettings() : PersistentSettings {
        const rtnVals =  this.ObjecitizeStringVals(this.SplitCookieValues(this.GetSettingsFromCookie()));
        return rtnVals as PersistentSettings;
    }

    private ObjecitizeStringVals(values:Array<string>) : Object {
        const returnObject : {[key:string] : any} = {};
        values.forEach(element => {
            if(!element) {return;}
            const nameValueSplit =  element.split(PersistentSettingsLoader.CookieValueDelim);
            console.log("Found cookie setting: " + nameValueSplit[0] + ", with value : " + nameValueSplit[1]);
            returnObject[nameValueSplit[0]] = nameValueSplit[1];
        });
        return returnObject;
    }

    private SplitCookieValues(cookie:string) : Array<string> {
        return cookie.split(PersistentSettingsLoader.CookiePartDelim);
    }

    private GetSettingsFromCookie() : string {
        return document.cookie;
    }

    private SaveSettingsFromCookie(cookieStr:string) : void {
        document.cookie = cookieStr;
    }

    public SaveSettings(settings :PersistentSettings) {
        let cookieStr = "";
        for(var prop in settings) {
            if(settings.hasOwnProperty(prop)) {
                cookieStr = cookieStr + prop + PersistentSettingsLoader.CookieValueDelim + settings[prop] + PersistentSettingsLoader.CookiePartDelim;
            }
        }
        console.log("Saving Cookie :" + cookieStr);
        this.SaveSettingsFromCookie(cookieStr);
    }
}