class Package(object):

    def __init__(self, data):
        self.id = data.get('key')
        self.name = data.get('title')
        self.type = data.get('settings').get('box')
        self.status = data.get('status').get('deliveryStatus')
        self.status_message = data.get('status').get('phase').get('message')
        self.delivery_date = data.get('status').get('delivery').get('deliveryDate')
        self.planned_date = None
        self.planned_from = None
        self.planned_to = None
        if data.get('status').get('enroute') is not None and data.get('status').get('enroute').get('timeframe') is not None:
            self.planned_date = data.get('status').get('enroute').get('timeframe').get('date')
            self.planned_from = data.get('status').get('enroute').get('timeframe').get('from')
            self.planned_to = data.get('status').get('enroute').get('timeframe').get('to')

        self.url = data.get('status').get('webUrl')

    def id(self):
        return self.id

    def name(self):
        return self.name

    def type(self):
        return self.type

    def status(self):
        return self.status

    def status_message(self):
        return self.status_message

    def delivery_date(self):
        return self.delivery_date

    def planned_date(self):
        return self.planned_date

    def planned_from(self):
        return self.planned_from

    def planned_to(self):
        return self.planned_to

    def url(self):
        return self.url
