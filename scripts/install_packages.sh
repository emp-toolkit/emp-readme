if [ "$(uname)" == "Darwin" ]; then
	brew update
	brew list openssl || brew install openssl
	brew list xctool || brew install xctool
	brew list pkg-config || brew install pkg-config
	brew list cmake || brew install cmake
	brew list gmp || brew install gmp
	brew list boost || brew install boost
else
	sudo apt-get install -y software-properties-common
	sudo apt-get update
	sudo apt-get install -y cmake git build-essential libssl-dev libgmp-dev python 
	sudo apt-get install -y libboost-dev
	sudo apt-get install -y libboost-{chrono,log,program-options,date-time,thread,system,filesystem,regex,test}-dev
fi
