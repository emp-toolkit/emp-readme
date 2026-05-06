#!/usr/bin/env python3
import subprocess, sys
install_packages = '''
if [ "$(uname)" == "Darwin" ]; then
	brew list openssl || brew install openssl
 	brew list pkg-config || brew install pkg-config
 	brew list cmake || brew install cmake
else
    if command -v apt-get >/dev/null; then
        sudo apt-get install -y software-properties-common
        sudo apt-get update
        sudo apt-get install -y cmake git build-essential libssl-dev
    elif command -v yum >/dev/null; then
        sudo yum install -y python3 gcc make git cmake gcc-c++ openssl-devel
    else
        echo "System not supported yet!"
    fi
fi
'''

install_template = '''
set -e
if [ -d X ]; then
    cd X
    git fetch origin
    git checkout Y
else
    git clone https://github.com/emp-toolkit/X.git --branch Y
    cd X
fi
cmake -S . -B build
cmake --build build -j
sudo cmake --install build
cd ..
'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-install', '--install', action='store_true')
parser.add_argument('-deps', '--deps', action='store_true')
parser.add_argument('--tool', nargs='?', const='main')
parser.add_argument('--ot', nargs='?', const='main')
parser.add_argument('--sh2pc', nargs='?', const='main')
parser.add_argument('--ag2pc', nargs='?', const='master')
parser.add_argument('--agmpc', nargs='?', const='master')
parser.add_argument('--zk', nargs='?', const='master')
args = parser.parse_args()

def run(cmd):
	if subprocess.call(["bash", "-c", cmd]) != 0:
		sys.exit(1)

if vars(args)['install'] or vars(args)['deps']:
	run(install_packages)

for k in ['tool', 'ot', 'zk', 'sh2pc', 'ag2pc', 'agmpc']:
	if vars(args)[k]:
		template = install_template.replace("X", "emp-"+k).replace("Y", vars(args)[k])
		print(template)
		run(template)
