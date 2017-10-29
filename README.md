# emp-tool
<img src="https://raw.githubusercontent.com/emp-toolkit/emp-readme/master/art/logo-full.jpg" width=300px/>

## Express Installation

1. Go the the folder you want to install everything

2. `wget https://goo.gl/wmt4KB -O install.sh && bash install.sh`

## Detailed Installation

1. Install related packages including `cmake git build-essential libssl-dev libgmp-dev`, or use this [script](https://github.com/emp-toolkit/emp-readme/blob/master/scripts/install_packages.sh).

2. Install [relic-toolkit](https://github.com/relic-toolkit/relic), or use this [script](https://github.com/emp-toolkit/emp-readme/blob/master/scripts/install_relic.sh).
Note that preset options for relic is for efficient ECC operations.

3. Install tools. Instruction can be found in the repo, or can be found [here](https://github.com/emp-toolkit/emp-readme/tree/master/scripts)

## Note for Mac Developers

1. Use Homebrew to install OpenSSL first. `brew install openssl`.

2. Specify `OPENSSL_ROOT_DIR` before installation, e.g., `export OPENSSL_ROOT_DIR=/usr/local/opt/openssl`. The root path can be found by `brew info openssl`.

## Documentation (under development)

https://emp-toolkit.github.io/emp-doc/

## Citation
```latex
    @misc{emp-toolkit,
      author = {Xiao Wang and Alex J. Malozemoff and Jonathan Katz},
      title = {{EMP-toolkit: Efficient MultiParty computation toolkit}},
      howpublished = {\url{https://github.com/emp-toolkit}},
      year={2016}
    }
```
