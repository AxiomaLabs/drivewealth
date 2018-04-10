from marshmallow import fields

from .base import BaseSchema


class InstrumentSchema(BaseSchema):
    instrument_id = fields.UUID(data_key='instrumentID')
    name = fields.String()
    symbol = fields.String()
    exchange_id = fields.String(data_key='exchangeID')
    trade_status = fields.Integer(data_key='tradeStatus')
    long_only = fields.Boolean(data_key='longOnly')
    prior_close = fields.Decimal(data_key='priorClose')
