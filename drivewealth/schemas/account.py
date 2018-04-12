from marshmallow import fields, post_load, Schema

from .base import BaseSchema
from .order import OrderSchema


class PositionSchema(Schema):
    initial_quantity = fields.Decimal(data_key='initQty')
    open_quantity = fields.Decimal(data_key='openQty')
    instrument_id = fields.UUID(data_key='instrumentID')
    cost_basis = fields.Decimal(data_key='costBasis')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Position', data)


class AccountSchema(Schema):
    account_id = fields.String(data_key='accountID')
    account_number = fields.String(data_key='accountNo')
    nickname = fields.String()
    currency_id = fields.String(data_key='currencyID')
    cash_available_for_withdrawal = fields.Decimal(
        data_key='rtCashAvailForWith')
    cash_available_for_trading = fields.Decimal(
        data_key='rtCashAvailForTrading')
    status = fields.Integer()
    type = fields.Integer(data_key='accountType')
    cash = fields.Decimal()
    default_goal_id = fields.UUID(data_key='defaultGoalID')
    free_trade_balance = fields.Decimal(data_key='freeTradeBalance')
    good_faith_violations = fields.Decimal(data_key='goodFaithViolations')
    ib_id = fields.UUID(data_key='ibID')
    interest_free = fields.Boolean(data_key='interestFree')
    margin = fields.Decimal(data_key='margin')
    opened_when = fields.String(data_key='openedWhen')
    pattern_day_trades = fields.Decimal(data_key='patternDayTrades')
    status = fields.Decimal(data_key='status')
    trading_type = fields.String(data_key='tradingType')
    updated_when = fields.String(data_key='updatedWhen')
    created_when = fields.String(data_key='createdWhen')
    positions = fields.Nested(PositionSchema, many=True)
    orders = fields.Nested(OrderSchema, many=True)

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
