import { Logging } from "../Logging";
import { DeviceInfo } from "../Models/DeviceInfo";

type SuccessCallback = JQuery.Ajax.SuccessCallback<any> | undefined;
type FailureCallback =  JQuery.Ajax.ErrorCallback<any> | undefined;

export class WindowAPI {

    public static GetMagicMirrorConfig(): JQuery.jqXHR {
        return Logging.ajaxQueryWithLogging(WindowAPI.CONFIG_URL, null, null);
    }

    public static GetApplicationList() {
        return Logging.ajaxQueryWithLogging(WindowAPI.APP_LIST_URL, null, null);
    }

    public static DeviceLogin(device: DeviceInfo, onComplete: SuccessCallback) {
        const query = Logging.ajaxQueryWithLoggingSettings({
            method: "POST",
            success: onComplete,
            url: WindowAPI.DEVICE_LOGIN_URL + device.id,
        });
        if (!query) {
            return $.ajax();
        } else {
            return query;
        }
    }

    public static CreateDevice(device: DeviceInfo, onComplete: SuccessCallback): JQuery.jqXHR {
        const query = Logging.ajaxQueryWithLoggingSettings({
            data: JSON.stringify(device),
            method: "POST",
            success: onComplete,
            url: WindowAPI.DEVICE_CREATE_URL,
        });
        if (!query) {
            return $.ajax();
        } else {
            return query;
        }
    }

    // tslint:disable-next-line: max-line-length
    public static GetDeviceInformation(deviceId: string, onComplete: SuccessCallback, onError: FailureCallback): JQuery.jqXHR  {
        const query = Logging.ajaxQueryWithLoggingSettings({
            error: onError,
            success: onComplete,
            url: this.DEVICE_URL + deviceId,
        });
        if (!query) {
            return $.ajax();
        } else {
            return query;
        }
    }

    private static readonly SERVER_URL = "";
    private static readonly APP_LIST_URL = WindowAPI.SERVER_URL + "/loadApplications";
    private static readonly APP_LOAD_URL = WindowAPI.SERVER_URL + "/loadApp/";
    private static readonly CONFIG_URL = WindowAPI.SERVER_URL + "/loadConfiguration";
    private static readonly DEVICE_URL = WindowAPI.SERVER_URL + "/loadDeviceData?deviceId=";
    private static readonly DEVICE_CREATE_URL = WindowAPI.SERVER_URL + "/devicecreate";
    private static readonly DEVICE_LOGIN_URL = WindowAPI.SERVER_URL + "/deviceLogin/?deviceId=";

}
