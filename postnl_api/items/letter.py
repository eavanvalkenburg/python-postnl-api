from datetime import datetime


class Letter(object):
    def __init__(self, data, documents):
        self.id = data.get("barcode")
        self.delivery_date = datetime.fromisoformat(data.get("expectedDeliveryDate"))
        self.status_message = None
        self.image = None

        if data.get("phase") is not None:
            self.status_message = data.get("phase").get("message")

        if len(documents.get("documents")) > 0:
            self.image = documents.get("documents")[0].get("link") + "?type=png"

    def id(self):
        return self.id

    def delivery_date(self):
        return self.delivery_date

    def status_message(self):
        return self.status_message

    def image(self):
        return self.image

    @property
    def debug_string(self):
        return f"{self.id} {self.status_message} {self.delivery_date.date()}"
