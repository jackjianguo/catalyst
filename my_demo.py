from catalyst import run_algorithm
from catalyst.api import order, record, symbols
import pandas as pd

from logbook import Logger
from catalyst.exchange.utils.stats_utils import get_pretty_stats

log = Logger('buy eth rt')
"""[summary]
['ada_usdt', 'algo_usdt', 'atom_usdt', 'bat_usdt', 'bch_usdt', 
'btc_usdt', 'comp_usdt', 'dash_usdt', 'eos_usdt', 'eth_usdt', 
'link_usdt', 'ltc_usdt', 'neo_usdt', 'trx_usdt', 'xlm_usdt', 
'xmr_usdt', 'xrp_usdt', 'xtz_usdt', 'zil_usdt', 'zrx_usdt']
"""

def initialize(context):
    log.info('=== initializing algo')
    context.assets = symbols(
        'ada_usdt', 'algo_usdt', 'atom_usdt', 'bat_usdt', 'bch_usdt', 
        'btc_usdt', 
        'comp_usdt', 
        'dash_usdt', 'eos_usdt', 'eth_usdt', 
        'link_usdt', 'ltc_usdt', 'neo_usdt', 'trx_usdt', 'xlm_usdt', 
        'xmr_usdt', 'xrp_usdt', 'xtz_usdt', 'zil_usdt', 'zrx_usdt'
    )
    context.nassets = len(context.assets)
    context.set_commission(maker=0.0004, taker=0.0004)
    context.set_slippage(slippage=0.0001)


def handle_data(context, data):
    log.info('=== handling bar {}'.format(data.current_dt))
    for b in context.assets:
        log.info(f'=== b: {b.symbol}')
        order(b, 1)



def analyze(context, stats):
    log.info('the daily stats:\n{}'.format(get_pretty_stats(stats)))
    pass


if __name__ == '__main__':
    # Index(['datetime', 'open', 'high', 'low', 'close', 'volume'], dtype='object')
    # data = pd.read_csv('/home/zjg/Binance_ethusdt.csv')
    # data['datetime'] = pd.to_datetime(data['datetime'], utc=True)
    # data = data[(data['datetime'] >= start) & (data['datetime'] <= end)]
    # data = data.set_index('datetime')

    start=pd.to_datetime('2020-07-31', utc=True)
    # end=pd.to_datetime('2021-01-01', utc=True)
    end = start

    run_algorithm(
        capital_base=10000,
        data_frequency='minute',
        initialize=initialize,
        handle_data=handle_data,
        exchange_name='binance',
        algo_namespace='buy_b',
        quote_currency='usdt',
        start=start,
        end=end,
        output='test.csv'
    )

