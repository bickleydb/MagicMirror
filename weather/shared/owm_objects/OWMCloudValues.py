
class OWMCloudValues:
    def __init__(self, date=0, cloud_status=""):
        self.cloud_status_value = cloud_status
        self.date = date

    def get_cloud_status(self):
        return self.cloud_status_value

    def get_date(self):
        return self.date
