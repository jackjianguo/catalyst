catalyst run -f buy_eth_rt.py --data-frequency minute -x binance -s 2020-01-01 -e 2020-01-02 -c usdt --capital-base 100000 -o buy_eth_rt_out.pickle

catalyst run -f buy_eth_rt.py -x poloniex -s 2016-1-1 -e 2017-2-1 -c usdt --capital-base 1000 -o test.pickle

catalyst ingest-exchange -x binance -f minute --csv ~/mockdata/binance_ethusdt.csv --show-progress

rtcatalyst ingest-exchange -x binance -f daily --csv ~/mockdata/binance_ethusdt.csv --show-progress

rtcatalyst run -f buy_eth_rt.py \
--data-frequency minute -x binance -s 2020-01-01 -e 2020-01-05 -c usdt --capital-base 10000 -o test.pickle

rtcatalyst run -f buy_btc_rt.py \
--data-frequency daily -x binance -s 2020-01-01 -e 2020-01-10 -c usdt --capital-base 10000 -o test.csv
