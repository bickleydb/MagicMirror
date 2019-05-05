import json
import home.models.MagicMirrorConfigModel as model


class MagicMirrorConfigResponse:

    def __init__(self, configValue):
        self.rows = configValue.rows
        self.columns = configValue.columns
        self.widthValue = configValue.width_value
        self.widthUnit = configValue.width_unit
        self.heightValue = configValue.height_value
        self.heightUnit = configValue.height_unit

    def to_json(self):
        return json.dumps({
         "rows": self.rows,
         "columns": self.columns,
         "widthValue": self.widthValue,
         "widthUnit": self.widthUnit,
         "heightValue": self.heightValue,
         "heightUnit": self.heightUnit,
        })
