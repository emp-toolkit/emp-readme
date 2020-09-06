#!/usr/python
import os
install_packages = '''
if [ "$(uname)" == "Darwin" ]; then
	brew update
	brew list openssl || brew install openssl
	brew list xctool || brew install xctool
	brew list pkg-config || brew install pkg-config
	brew list cmake || brew install cmake
else
	sudo apt-get install -y software-properties-common
	sudo apt-get update
	sudo apt-get install -y cmake git build-essential libssl-dev
fi
'''

install_template = '''
git clone https://github.com/emp-toolkit/X.git
cd X
cmake .
make -j4
sudo make install
cd ..
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-install', '--install', action='store_true')
parser.add_argument('-tool', '--tool', action='store_true')
parser.add_argument('-ot', '--ot', action='store_true')
parser.add_argument('-sh2pc', '--sh2pc', action='store_true')
parser.add_argument('-ag2pc', '--ag2pc', action='store_true')
parser.add_argument('-agmpc', '--agmpc', action='store_true')
args = parser.parse_args()

for k in ['install', 'tool', 'ot', 'sh2pc', 'ag2pc', 'agmpc']:
	if vars(args)[k]:
		if k == "install":
			os.system(install_packages)
		#	print install_packages
		else:
			os.system(install_template.replace("X", "emp-"+k))
		#	print install_template.replace("X", "emp-"+k)
