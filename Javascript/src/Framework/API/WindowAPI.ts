import { Logging } from '../Logging';
import { DeviceInfo } from '../Models/DeviceInfo';

export class WindowAPI {


    private static readonly SERVER_URL = "";
    private static readonly APP_LIST_URL = WindowAPI.SERVER_URL + "/loadApplications";
    private static readonly APP_LOAD_URL = WindowAPI.SERVER_URL + "/loadApp/";
    private static readonly CONFIG_URL = WindowAPI.SERVER_URL + "/loadConfiguration";
    private static readonly DEVICE_URL = WindowAPI.SERVER_URL + "/loadDeviceData?deviceId=";
    private static readonly DEVICE_CREATE_URL = WindowAPI.SERVER_URL + "/devicecreate";
    private static readonly DEVICE_LOGIN_URL = WindowAPI.SERVER_URL + "/deviceLogin/?deviceId="
 

    public static GetMagicMirrorConfig(onComplete: JQuery.Ajax.SuccessCallback<any>) : JQuery.jqXHR {
        return Logging.ajaxQueryWithLogging(WindowAPI.CONFIG_URL, onComplete, null);
    }

    public static GetApplicationList() {
        return Logging.ajaxQueryWithLogging(WindowAPI.APP_LIST_URL, null, null);
    }

    public static DeviceLogin(device:DeviceInfo, onComplete: JQuery.Ajax.SuccessCallback<any> | undefined) {
        const query = Logging.ajaxQueryWithLoggingSettings({
            url: WindowAPI.DEVICE_LOGIN_URL + device.id,
            method: "POST", 
            success: onComplete
        })
        if(!query) {
            return $.ajax();
        } else {
            return query;
        }
    }

    public static CreateDevice(device:DeviceInfo, onComplete: JQuery.Ajax.SuccessCallback<any> | undefined) : JQuery.jqXHR {
        const query = Logging.ajaxQueryWithLoggingSettings({
            url: WindowAPI.DEVICE_CREATE_URL,
            method: "POST",
            data: JSON.stringify(device),
            success: onComplete
        })
        if(!query) {
            return $.ajax();
        } else {
            return query;
        }
    }

    public static GetDeviceInformation(deviceId:string, onComplete: JQuery.Ajax.SuccessCallback<any> | undefined , onError: JQuery.Ajax.ErrorCallback<any> | undefined) : JQuery.jqXHR  {
        const query = Logging.ajaxQueryWithLoggingSettings({
            url: this.DEVICE_URL + deviceId,
            success: onComplete,
            error: onError
        });
        if(!query) {
            return $.ajax();
        } else {
            return query;
        }
    }


}