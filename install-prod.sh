sudo apt-get install libatlas-base-dev python-dev gfortran pkg-config libfreetype6-dev

conda env remove --name catalyst

conda create --name catalyst python=3.6 scipy zlib

conda activate catalyst

pip install setuptools==45

conda install --name catalyst --freeze-installed bcolz

pip install enigma-catalyst matplotlib

pip install numpy==1.17.0

pip uninstall enigma-catalyst

# 编译时安装
pip install -e workspace/catalyst

# pip freeze 会自动生成request.txt 文件
pip freeze

pip install -r requestments.txt

# unzip market data
tar -zxvf market/catalyst.tar.gz
mv .catalyst ~/

touch -c ~/.catalyst/data/exchanges/binance/cctx_markets.json

# ingest data
catalyst ingest-exchange -x binance -f minute --csv market/binance_future_btcusdt_minute.csv --show-progress

# run
catalyst run -f demo/buy_btc_rt.py --data-frequency minute -x binance -s 2020-01-01 -e 2020-01-01\
-c usdt --capital-base 1000 -o test.csv


