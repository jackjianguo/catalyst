"""
    This is a very simple example referenced in the beginner's tutorial:
    https://enigmampc.github.io/catalyst/beginner-tutorial.html

    Run this example, by executing the following from your terminal:
      catalyst ingest-exchange -x bitfinex -f daily -i btc_usdt
      catalyst run -f buy_btc_simple.py -x bitfinex --start 2016-1-1 \
        --end 2017-9-30 -o buy_btc_simple_out.pickle

    If you want to run this code using another exchange, make sure that
    the asset is available on that exchange. For example, if you were to run
    it for exchange Poloniex, you would need to edit the following line:

        context.asset = symbol('btc_usdt')     # note 'usdt' instead of 'usd'

    and specify exchange poloniex as follows:
    catalyst ingest-exchange -x poloniex -f daily -i btc_usdt
    catalyst run -f buy_btc_simple.py -x poloniex --start 2016-1-1 \
        --end 2017-9-30 -o buy_btc_simple_out.pickle

    To see which assets are available on each exchange, visit:
    https://www.enigma.co/catalyst/status
"""
from catalyst import run_algorithm
from catalyst.api import order, record, symbol
import pandas as pd

from logbook import Logger
from catalyst.exchange.utils.stats_utils import get_pretty_stats

log = Logger('buy eth rt')

def initialize(context):
    log.info('=== initializing algo')
    context.asset = symbol('btc_usdt')
    context.set_commission(maker=0.0004, taker=0.0004)
    context.set_slippage(slippage=0.0001)


def handle_data(context, data):
    log.info('=== handling bar {}'.format(data.current_dt))
    order(context.asset, 1)
    record(btc=data.current(context.asset, 'price'))


def analyze(context, stats):
    log.info('the daily stats:\n{}'.format(get_pretty_stats(stats)))
    pass


if __name__ == '__main__':
    # Index(['datetime', 'open', 'high', 'low', 'close', 'volume'], dtype='object')
    # data = pd.read_csv('/home/zjg/Binance_ethusdt.csv')
    # data['datetime'] = pd.to_datetime(data['datetime'], utc=True)
    # data = data[(data['datetime'] >= start) & (data['datetime'] <= end)]
    # data = data.set_index('datetime')

    start=pd.to_datetime('2020-01-01', utc=True)
    end=pd.to_datetime('2020-01-01', utc=True)

    run_algorithm(
        capital_base=10000,
        data_frequency='minute',
        initialize=initialize,
        handle_data=handle_data,
        exchange_name='binance',
        algo_namespace='buy_eth_rt',
        quote_currency='usdt',
        start=start,
        end=end,
        output='test.csv'
    )

