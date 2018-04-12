class InstrumentNotFoundError(Exception):
    def __init__(self, exception, instrument_id):
        super(InstrumentNotFoundError, self).__init__(exception)
        self.instrument_id = instrument_id


class OrderNotFoundError(Exception):
    def __init__(self, exception, order_id):
        super(OrderNotFoundError, self).__init__(exception)
        self.order_id = order_id
