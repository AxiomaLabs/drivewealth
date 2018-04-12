from marshmallow import fields, post_load, Schema

from .base import BaseSchema


class OrderSchema(Schema):
    order_id = fields.UUID(load_from='orderID')
    commission = fields.Decimal()
    order_number = fields.String(load_from='orderNo')
    order_quantity = fields.Decimal(load_from='orderQty')
    order_status = fields.String(load_from='ordStatus')
    price = fields.Decimal()
    limit_price = fields.Decimal(load_from='limitPrice')
    resting_order_expires = fields.DateTime(
        load_from='isoTimeRestingOrderExpires')
    amount_cash = fields.Decimal(load_from='amountCash')
    rate_ask = fields.Decimal(load_from='rateAsk')
    rate_bid = fields.Decimal(load_from='rateBid')
    instrument_id = fields.UUID(load_from='instrumentID')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Order', data)
