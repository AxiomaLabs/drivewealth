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


class MarketOrderSchema(Schema):
    order_id = fields.String(load_from='orderID')
    instrument_id = fields.String(load_from='instrumentID')
    leaves_quantity = fields.String(load_from='leavesQty')
    ord_type = fields.String(load_from='ordType')
    side = fields.String(load_from='side')
    limit_price = fields.String(load_from='limitPrice')
    time_in_force = fields.String(load_from='timeInForce')
    expire_timestamp = fields.String(load_from='expireTimestamp')
    status_path = fields.String(load_from='statusPath')
