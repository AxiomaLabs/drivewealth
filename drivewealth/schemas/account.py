from marshmallow import fields, post_load, Schema

from .base import BaseSchema


class OrderSchema(Schema):
    order_id = fields.UUID(data_key='orderID')
    commission = fields.Decimal()
    order_number = fields.String(data_key='orderNo')
    order_quantity = fields.Decimal(data_key='orderQty')
    order_status = fields.String(data_key='ordStatus')
    price = fields.Decimal()
    limit_price = fields.Decimal(data_key='limitPrice')
    resting_order_expires = fields.DateTime(
        data_key='isoTimeRestingOrderExpires')
    amount_cash = fields.Decimal(data_key='amountCash')
    rate_ask = fields.Decimal(data_key='rateAsk')
    rate_bid = fields.Decimal(data_key='rateBid')
    instrument_id = fields.UUID(data_key='instrumentID')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Order', data)


class PositionSchema(Schema):
    initial_quantity = fields.Decimal(data_key='initQty')
    open_quantity = fields.Decimal(data_key='openQty')
    instrument_id = fields.UUID(data_key='instrumentID')
    cost_basis = fields.Decimal(data_key='costBasis')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Position', data)


class AccountSchema(Schema):
    id = fields.String(data_key='accountID')
    currency_id = fields.String(data_key='currencyID')
    cash_available_for_withdrawal = fields.Decimal(
        data_key='rtCashAvailForWith')
    cash_available_for_trading = fields.Decimal(
        data_key='rtCashAvailForTrading')
    status = fields.Integer()
    positions = fields.Nested(PositionSchema, many=True)
    orders = fields.Nested(OrderSchema, many=True)
    type = fields.Integer(data_key='accountType')
    cash = fields.Decimal()
    account_number = fields.String(data_key='accountNo')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Account', data)


class SessionSchema(BaseSchema):
    session_key = fields.String(data_key='sessionKey')
    user_id = fields.UUID(data_key='userID')
    accounts = fields.Nested(AccountSchema, many=True)
