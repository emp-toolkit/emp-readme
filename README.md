# emp-tool
<img src="https://raw.githubusercontent.com/emp-toolkit/emp-readme/master/art/logo-full.jpg" width=300px/>

## Express Installation

1. Go the the folder you want to install everything

2. `wget https://goo.gl/wmt4KB -O install.sh && bash install.sh`

## Detailed Installation

1. Install related packages including `cmake git build-essential libssl-dev libgmp-dev` (for Linux), or `openssl xctool pkg-config cmake gmp boost` (for Mac), or use this [script](https://github.com/emp-toolkit/emp-readme/blob/master/scripts/install_packages.sh).

2. Install [relic-toolkit](https://github.com/relic-toolkit/relic), or use this [script](https://github.com/emp-toolkit/emp-readme/blob/master/scripts/install_relic.sh).
Note that preset options for relic is for efficient ECC operations.

3. Install tools. Instruction can be found in the repo, or can be found [here](https://github.com/emp-toolkit/emp-readme/tree/master/scripts)

## Note for Mac Developers

1. Use Homebrew to install OpenSSL first. `brew install openssl`.

2. Add the pkgconfig file of OpenSSL to `PKG_CONFIG_PATH`, e.g., `export PKG_CONFIG_PATH=${PKG_CONFIG_PATH}:/usr/local/opt/openssl/lib/pkgconfig`. The pkg-config path can be found by `brew info openssl`.

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
## Acknowledgement
This work was supported in part by the National Science Foundation under Awards #1111599 and #1563722.
