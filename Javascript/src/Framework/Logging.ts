import { Logger } from "./Logger";

type ErrorCallback = JQuery.Ajax.ErrorCallback<any> | Array<JQuery.Ajax.ErrorCallback<any>> | null;
type SuccessCallback =  JQuery.Ajax.SuccessCallback<any> | Array<JQuery.Ajax.SuccessCallback<any>> |  null;
export class Logging {

    public static ajaxQueryWithLoggingSettings(settings: JQueryAjaxSettings): JQuery.jqXHR | null {
        if (!settings.url) {
            return null;
        }
        if (settings.success) {
            settings.success = Logging.SuccessCallback.bind(self, settings.url, settings.success);
        }
        if (settings.error) {
            settings.error = Logging.ErrorCallback.bind(self, settings.url, settings.error);
        }
        return $.ajax(settings);
    }

    // tslint:disable-next-line: max-line-length
    public static ajaxQueryWithLogging(url: string, successCallback: SuccessCallback, errorCallback: ErrorCallback): JQuery.jqXHR {
        let internalSuccessCallback: JQuery.Ajax.SuccessCallback<any> | undefined;
        if (successCallback != null) {
            internalSuccessCallback = Logging.SuccessCallback.bind(self, url, successCallback);
        }

        let internalErrorCallback: JQuery.Ajax.ErrorCallback<any> | undefined;
        if (errorCallback != null) {
            internalErrorCallback = Logging.ErrorCallback.bind(self, url, errorCallback);
        }
        return $.ajax(url, {
            error: internalErrorCallback,
            success:  internalSuccessCallback,
        });
    }

    // tslint:disable-next-line: max-line-length
    private static ErrorCallback(url: string, innerCallback: ErrorCallback, jqXHRObject: JQuery.jqXHR, status: JQuery.Ajax.ErrorTextStatus, errorText: string)  {
        Logger.Instance.LogError("Call to " + url + " failed with an error: " + errorText);
        if (Array.isArray(innerCallback) && innerCallback) {
            innerCallback.forEach( (callback: ErrorCallback) => {
                if (callback instanceof Array) {
                    for (const callbackInstance of callback) {
                        callbackInstance(jqXHRObject, status, errorText);
                    }
                } else if (callback) {
                    callback(jqXHRObject, status, errorText);
                }
            });
            return;
        }
        if (innerCallback) {
            innerCallback.call(self, jqXHRObject, status, errorText);
        }
    }

    // tslint:disable-next-line: max-line-length
    private static SuccessCallback(url: string, innerCallback: SuccessCallback, data: any, status: JQuery.Ajax.SuccessTextStatus, jqXHRObject: JQuery.jqXHR)  {
        Logger.Instance.LogInformational("Call to " + url + " succcessful");
        if (innerCallback == null) {return; }
        if (Array.isArray(innerCallback)) {
            for (const callback of innerCallback)  {
                callback.call(this, data, status, jqXHRObject);
            }
            return;
        }
        innerCallback.call(this, data, status, jqXHRObject);
    }
}
