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


class UserSchema(BaseSchema):
    user_id = fields.String(data_key='userID')
    avatar_url = fields.String(data_key='avatarUrl')
    coin_balance = fields.Decimal(data_key='coinBalance')
    commission_rate = fields.Decimal(data_key='commissionRate')
    country_id = fields.String(data_key='countryID')
    display_name = fields.String(data_key='displayName')
    email_address1 = fields.String(data_key='emailAddress1')
    email_address = fields.String(data_key='emailAddress')
    first_name = fields.String(data_key='firstName')
    language_id = fields.String(data_key='languageID')
    last_name = fields.String(data_key='lastName')
    referral_code = fields.String(data_key='referralCode')
    username = fields.String(data_key='username')


class SessionSchema(BaseSchema):
    session_key = fields.String(data_key='sessionKey')
    user_id = fields.UUID(data_key='userID')
    user = fields.Nested(UserSchema, many=True)
    accounts = fields.Nested(AccountSchema, many=True)
