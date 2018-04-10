from cachetools.func import ttl_cache

from ..schemas import create_object_from_json_response


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
        """
        params = {
            'symbol': symbol,
            'name': name,
            'tag': tag,
        }
        res = self.drive_wealth.instruments.GET(params=params)
        return create_object_from_json_response('Instrument', res, many=True)
