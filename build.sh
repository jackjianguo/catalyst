#python setup.py build_ext --inplace

sudo apt-get install libatlas-base-dev python-dev gfortran pkg-config libfreetype6-dev

conda create --name py36 python=3.6 scipy zlib

conda activate py36

conda install --name py36 --freeze-installed bcolz

pip install workspace/github/catalyst

rtcatalyst

.catalyst/data/exchanges/binance/cctx_markets.json
.catalyst/data/exchanges/binance/symbols.json
.catalyst/data/exchanges/binance/symbols_local.json


