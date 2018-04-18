import json

from requests.exceptions import HTTPError

from .exceptions import OrderNotFoundError
from ..schemas import create_object_from_json_response


class OrderApiMixin:

    def get_order_status(self, order_id):
        """
        Get specific order status.
        A market order is successfully accepted when:
        1. "orderQty" is equal to "leavesQty".
        2. "execType" and "ordStatus" are both equal to "0".
        @Parmas
            order_id - String
        @Return
            orderID
            accountID
            userID
            cumQty
            accountNo
            commission
            createdByID
            createdWhen
            execType
            grossTradeAmt
            instrumentID
            lastPx
            lastQty
            leavesQty
            orderNo
            orderQty
            ordStatus
            ordType
            price
            rateAsk
            rateBid
            side
            accountType
            autoStop
            limitPrice
            timeInForce
            isoTimeRestingOrderExpires
            internalMemo
            amountCash
        """
        response = self.drive_wealth.orders(order_id).GET()
        try:
            return create_object_from_json_response('Order', response)
        except HTTPError, e:
            raise OrderNotFoundError(e, order_id)

    def create_market_order(
            self, instrument_id, account_id, account_number, user_id,
            side, order_quantity, amount_cash, account_type='2'):
        """
        Add a new market order.
        @Params
            instrument_id
            account_id
            account_number
            user_id
            account_type
            ord_type
            side
            order_quantity
            amount_cash
        @return
            orderID
            instrumentID
            leavesQty
            ordType
            side
            limitPrice
            timeInForce
            expireTimestamp
            statusPath
        """
        params = {
            'instrumentID': instrument_id,
            'accountID': account_id,
            'accountNo': account_number,
            'userID': user_id,
            'accountType': account_type,
            'ordType': "1",
            'side': side,
            'orderQty': order_quantity,
            'amountCash': amount_cash,
        }
        response = self.drive_wealth.orders(data=json.dumps(params)).POST()
        return create_object_from_json_response('MarketOrder', response)
