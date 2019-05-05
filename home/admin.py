from django.contrib import admin

# Register your models here.
from django.contrib import admin

from home.models.ModelExtender.PhoneNumberModel import PhoneNumberModel

from .models import ApplicationCSSFileBridgeModel as CSSFileBridge
from .models import ApplicationDefinitionModel as AppDef
from .models import ApplicationUIBridgeModel as AppUIBridge
from .models import ApplicationUIConfigModel as AppUIConfig
from .models import CSSResourceModel as CSS
from .models import FontModel as Fonts
from .models import MagicMirrorConfigModel as MagicMirrorConfig
from .models import UserAppListBridgeModel as UserAppList
from .models import User
from .models import Device
from .models import UserDeviceBridge
# Register your models here.
admin.site.register(AppDef.ApplicationDefinitionModel)
admin.site.register(CSSFileBridge.ApplicationCSSFileBridgeModel)
admin.site.register(CSS.CSSResourceModel)
admin.site.register(MagicMirrorConfig.MagicMirrorConfigModel)
admin.site.register(Fonts.FontModel)
admin.site.register(AppUIConfig.ApplicationUIConfigModel)
admin.site.register(AppUIBridge.ApplicationUIBridgeModel)
admin.site.register(UserAppList.UserAppListBridgeModel)
admin.site.register(PhoneNumberModel)
admin.site.register(User.MagicMirrorUser)
admin.site.register(Device.DeviceModel)
admin.site.register(UserDeviceBridge.UserDeviceBridge)
