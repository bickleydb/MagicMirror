
export class Logging {

    public static ajaxQueryWithLoggingSettings(settings: JQueryAjaxSettings) : JQuery.jqXHR | null {
        if(!settings.url) {
            return null;
        }
        if(settings.success) {
            settings.success = Logging.SuccessCallback.bind(self, settings.url, settings.success);
        }
        if(settings.error) {
            settings.error = Logging.ErrorCallback.bind(self, settings.url, settings.error);
        }
        return $.ajax(settings);
    }

    private static ErrorCallback(url: string, innerCallback:JQuery.Ajax.ErrorCallback<any> | JQuery.Ajax.ErrorCallback<any>[], jqXHRObject: JQuery.jqXHR,status :JQuery.Ajax.ErrorTextStatus, errorText:string)  {
        console.error("Call to " + url + " failed with an error: " + errorText);
        if(Array.isArray(innerCallback)) {
            innerCallback.forEach( (callback : JQuery.Ajax.ErrorCallback<any>) => callback.call(self, jqXHRObject, status, errorText));
            return;
        }
        innerCallback.call(self, jqXHRObject, status, errorText);
    }

    private static SuccessCallback(url: string, innerCallback:JQuery.Ajax.SuccessCallback<any> | JQuery.Ajax.SuccessCallback<any>[], data:any, status :JQuery.Ajax.SuccessTextStatus, jqXHRObject: JQuery.jqXHR)  {
        console.log("Call to " + url + " succcessful");
        if(Array.isArray(innerCallback)) {
            for(let index = 0; index < innerCallback.length; index++) {
                innerCallback[index].call(this,data,status,jqXHRObject);
            }
            return;
        }
        innerCallback.call(this,data, status, jqXHRObject);
    }


    public static ajaxQueryWithLogging(url: string, successCallback: JQuery.Ajax.SuccessCallback<any> | null, errorCallback: JQuery.Ajax.ErrorCallback<any> | null): JQuery.jqXHR {
        let internalSuccessCallback: JQuery.Ajax.SuccessCallback<any> | undefined;
        if (successCallback != null) {
            internalSuccessCallback = Logging.SuccessCallback.bind(self, url, successCallback);
        }

        let internalErrorCallback: JQuery.Ajax.ErrorCallback<any> | undefined;
        if (errorCallback != null) {
            internalErrorCallback = Logging.ErrorCallback.bind(self, url, errorCallback);
        }
        return $.ajax(url, {
            success:  internalSuccessCallback,
            error: internalErrorCallback
        })
    }
}