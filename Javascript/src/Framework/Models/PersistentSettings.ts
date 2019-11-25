import { Logger } from "../Logger";
import { Logging } from "../Logging";

// tslint:disable-next-line: interface-name
export interface PersistentSettings {
    magicMirrorId: string | undefined;
    csrftoken: string | undefined;
    [key: string]: string | undefined;
}

export class PersistentSettingsLoader {
    public static readonly CookiePartDelim = ",";
    public static readonly CookieValueDelim = "=";

    private logger: Logger  = Logger.Instance;

    public LoadSettings(): PersistentSettings {
        const rtnVals =  this.ObjecitizeStringVals(this.SplitCookieValues(this.GetSettingsFromCookie()));
        return rtnVals as PersistentSettings;
    }

    public SaveSettings(settings: PersistentSettings) {
        let cookieStr = "";
        for (const prop in settings) {
            if (settings.hasOwnProperty(prop)) {
                cookieStr = cookieStr +
                prop +
                PersistentSettingsLoader.CookieValueDelim +
                settings[prop] +
                PersistentSettingsLoader.CookiePartDelim;
            }
        }

        this.logger.LogInformational("Saving Cookie :" + cookieStr);
        this.SaveSettingsFromCookie(cookieStr);
    }

    private ObjecitizeStringVals(values: string[]): object {
        const returnObject: {[key: string]: any} = {};
        values.forEach((element) => {
            if (!element) {return; }
            const nameValueSplit =  element.split(PersistentSettingsLoader.CookieValueDelim);
            this.logger.LogInformational(
                "Found cookie setting: " + nameValueSplit[0] + ", with value : " + nameValueSplit[1]);
            returnObject[nameValueSplit[0]] = nameValueSplit[1];
        });
        return returnObject;
    }

    private SplitCookieValues(cookie: string): string[] {
        return cookie.split(PersistentSettingsLoader.CookiePartDelim);
    }

    private GetSettingsFromCookie(): string {
        return document.cookie;
    }

    private SaveSettingsFromCookie(cookieStr: string): void {
        document.cookie = cookieStr;
    }
}
