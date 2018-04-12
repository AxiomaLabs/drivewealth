from cachetools.func import ttl_cache
from requests.exceptions import HTTPError

from ..schemas import create_object_from_json_response
from .exceptions import InstrumentNotFoundError


class InstrumentApiMixin:

    @ttl_cache(maxsize=128, ttl=60*15, typed=True)
    def search_instruments(self, symbol=None, name=None, tag=None):
        """
        Searches for a particular instrument by symbol, name, or tag.
        @Params
            symbol - String
            name - String
            tag - String
        @Return list of instruments.
            instrumentID
            name
            category
            currencyID
            exchangeID
            limitStatus
            instrumentTypeID
            isLongOnly
            marginCurrencyID
            orderSizeMax
            orderSizeMin
            orderSizeStep
            rateAsk
            rateBid
            ratePrecision
            symbol
            tags - List
            tradeStatus
            tradingHours
            uom
            urlImage
            urlInvestor
            chaikinPgr
            sector
            priorClose
            nameLower
            underlyingID
            marketState
            minTic
            pipMultiplier
            tickerSymbol
            rebateSpread
            longOnly
        """
        params = {
            'symbol': symbol,
            'name': name,
            'tag': tag,
        }
        response = self.drive_wealth.instruments.GET(params=params)
        return create_object_from_json_response(
            'Instrument', response, many=True)

    @ttl_cache(maxsize=128, ttl=60*15)
    def get_instrument(self, instrument_id):
        """
        Gets a particular instrument by instrument id.
        Returns an instrument or 404 if not found.
        @Params
            instrument_id - UUID
        @Return
            instrumentID
            name
            currencyID
            description
            exchangeID
            limitStatus
            instrumentTypeID
            isLongOnly
            marginCurrencyID
            orderSizeMax
            orderSizeMin
            orderSizeStep
            rateAsk
            rateBid
            ratePrecision
            symbol
            tags - List
            tradeStatus
            tradingHours
            uom
            urlImage
            urlInvestor
            sector
            priorClose
            nameLower
            underlyingID
            marketState
            minTic
            pipMultiplier
            tickerSymbol
            rebateSpread
            longOnly
        """
        params = {
            'options': 'F',  # get the fundamental data
        }
        response = self.drive_wealth.instruments(
            instrument_id).GET(params=params)

        try:
            return create_object_from_json_response(
                'Instrument', response, many=False)
        except HTTPError, e:
            raise InstrumentNotFoundError(e, instrument_id)

    @ttl_cache(maxsize=128, ttl=60*15)
    def get_instruments(self, trade_status="1"):
        """
        Get a list of instruments
        @Params
            trade_status: -1 all, 0 Inactive, 1 Active, 2 Close Only
        @Return list of instruments
            instrumentID
            name
            currencyID
            exchangeID
            limitStatus
            instrumentTypeID
            isLongOnly
            marginCurrencyID
            orderSizeMax
            orderSizeMin
            orderSizeStep
            ratePrecision
            symbol
            tags - List
            tradeStatus
            tradingHours
            uom
            urlInvestor
            chaikinPgr
            priorClose
            nameLower
            underlyingID
            marketState
            minTic
            pipMultiplier
            rebateSpread
            longOnly
        """
        params = {'tradeStatus': trade_status}
        response = self.drive_wealth.instruments().GET(params=params)
        return create_object_from_json_response(
            'Instrument', response, many=True)
