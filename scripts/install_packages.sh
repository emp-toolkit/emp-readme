if [ "$(uname)" == "Darwin" ]; then
	brew update
	brew install openssl
	brew install xctool
	brew install cmake
	brew install gmp
	brew install boost
else
	sudo apt-get install -y software-properties-common
	sudo add-apt-repository -y ppa:george-edison55/cmake-3.x
	sudo apt-get update
	sudo apt-get install -y cmake git build-essential libssl-dev libgmp-dev python libboost-all-dev
fi
