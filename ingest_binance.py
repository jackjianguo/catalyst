# catalyst ingest-exchange -x binance -f minute --csv market/binance_future_btcusdt_minute.csv --show-progress

import os
import sys
import subprocess
import pandas as pd

path = '~/mockdata/binance_future/binance_future'

"""[summary]
['ada_usdt', 'algo_usdt', 'atom_usdt', 'bat_usdt', 'bch_usdt', 
'btc_usdt', 'comp_usdt', 'dash_usdt', 'eos_usdt', 'eth_usdt', 
'link_usdt', 'ltc_usdt', 'neo_usdt', 'trx_usdt', 'xlm_usdt', 
'xmr_usdt', 'xrp_usdt', 'xtz_usdt', 'zil_usdt', 'zrx_usdt']
"""

def update():
    cmd = 'touch -c ~/.catalyst/data/exchanges/binance/cctx_markets.json'
    print(cmd)
    subprocess.run(cmd, shell=True, check=True)


def parse_data(fp):
    df = pd.read_csv(fp)
    df = df[df['last_traded'] < '2020-08-01 00:00']
    df = df.sort_values(by='last_traded')
    df = df.drop_duplicates().reset_index(drop=True)
    print(fp, '\n', ', init:', df['last_traded'].min(), ', end:', df['last_traded'].max())
    df.to_csv(fp, index=False)
    if len(df) > 0:
        test_list.append(df.iloc[0]['symbol'])
    return len(df) > 0


def ingest():
    files = os.listdir(path)
    files.sort()
    files = [f for f in files if 'min' in f]
    file_path = [os.path.join(path, f) for f in files]
    n = len(file_path)
    i = 0
    for fp in file_path:
        i += 1
        if not parse_data(fp):
            continue
        cmd = f'catalyst ingest-exchange -x binance -f minute --csv {fp} --show-progress'
        print(i, '/', n, end=', ')
        print(cmd)
        print()
        subprocess.run(cmd, shell=True, check=True)
    pass

if __name__ == '__main__':
    test_list = []
    update()
    ingest()
    print(test_list)
    pass

