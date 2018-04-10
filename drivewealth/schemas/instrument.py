from marshmallow import fields

from .base import BaseSchema


class InstrumentSchema(BaseSchema):
    instrument_id = fields.UUID(load_from='instrumentID')
    name = fields.String()
    symbol = fields.String()
    exchange_id = fields.String(load_from='exchangeID')
    trade_status = fields.Integer(load_from='tradeStatus')
    long_only = fields.Boolean(load_from='longOnly')
    prior_close = fields.Decimal(load_from='priorClose')
    order_size_maximum = fields.Decimal(load_from='orderSizeMax')
    order_size_minimum = fields.Decimal(load_from='orderSizeMin')
    order_size_step = fields.Decimal(load_from='orderSizeStep')
    rate_ask = fields.Decimal(load_from='rateAsk')
    rate_bid = fields.Decimal(load_from='rateBid')
