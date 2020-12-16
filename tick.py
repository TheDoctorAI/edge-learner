""" A ticker proxy seems like a good idea but not that important yet """
import asyncio
import os
import sys
from pprint import pprint


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt.async_support as ccxt  # noqa: E402

pprint(asyncio.get_event_loop().run_until_complete(ccxt.binance().fetch_ticker('ETH/BTC')))
