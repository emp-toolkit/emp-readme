#!/usr/python
import subprocess
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
git clone https://github.com/emp-toolkit/X.git --branch Y
cd X
cmake .
make -j4
sudo make install
cd ..
'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-install', '--install', action='store_true')
parser.add_argument('-deps', '--deps', action='store_true')
parser.add_argument('--tool', nargs='?', const='master')
parser.add_argument('--ot', nargs='?', const='master')
parser.add_argument('--sh2pc', nargs='?', const='master')
parser.add_argument('--ag2pc', nargs='?', const='master')
parser.add_argument('--agmpc', nargs='?', const='master')
parser.add_argument('--zk', nargs='?', const='master')
args = parser.parse_args()

if vars(args)['install'] or vars(args)['deps']:
	subprocess.call(["bash", "-c", install_packages])

for k in ['tool', 'ot', 'zk', 'sh2pc', 'ag2pc', 'agmpc']:
	if vars(args)[k]:
		template = install_template.replace("X", "emp-"+k).replace("Y", vars(args)[k])
		print(template)
		subprocess.call(["bash", "-c", template])
