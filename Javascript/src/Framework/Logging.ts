export class Logging {
    
   public static ajaxQueryWithLogging(url: string, successCallback: JQuery.Ajax.SuccessCallback<any> | null, errorCallback: JQuery.Ajax.ErrorCallback<any> | null): JQueryStatic {

    let internalSuccessCallback: JQuery.Ajax.SuccessCallback<any> | undefined = undefined;
    if (successCallback != null) {
        internalSuccessCallback = function (userCallback: JQuery.Ajax.SuccessCallback<any>, data: any, status: JQuery.Ajax.SuccessTextStatus, jqXHRObject: JQueryXHR) {
            console.log("Call to " + url + " succcessful");
            userCallback.call(self, data, status, jqXHRObject);
        }.bind(self, successCallback);
    }

    let internalErrorCallback: JQuery.Ajax.ErrorCallback<any> | undefined = undefined;
    if (errorCallback != null) {
        internalErrorCallback = function (userCallback: JQuery.Ajax.ErrorCallback<any>, JQueryXHRObject: JQueryXHR, status: JQuery.Ajax.ErrorTextStatus, errString: string) {
            console.error("Call to " + url + " failed with error " + errString);
            errorCallback.call(self, JQueryXHRObject, status, errString);
        }.bind(self, errorCallback);
    }
    $.ajax(url, {
        success: internalSuccessCallback,
        error: internalErrorCallback
    })
    return $;
}
}