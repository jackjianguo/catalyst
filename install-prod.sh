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




