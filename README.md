# EMP Toolkit Readme Page
<img src="https://raw.githubusercontent.com/emp-toolkit/emp-readme/v0.3.x/art/logo-full.jpg" width=300px/>

## Installation

Requires Ubuntu 22.04+ (or comparable) with CMake, a C++17 compiler, OpenSSL, and Python 3. Tested with cmake 3.22 / gcc 11 on Ubuntu 22.04.

1. Go to the folder you want to install everything

2. `curl https://raw.githubusercontent.com/emp-toolkit/emp-readme/v0.3.x/scripts/install.py -O`

3. `python3 install.py --deps --tool --ot` to install code dependencies plus the `v0.3.x` branch of emp-tool and emp-ot. More flags can be added including `--sh2pc`, `--ag2pc`, `--agmpc`, `--zk`. `--tool` / `--ot` / `--sh2pc` / `--ag2pc` / `--zk` default to `v0.3.x` on this branch; `--agmpc` defaults to `master` because emp-agmpc has no v0.3.x branch yet.
- You can override the branch per repo, e.g. `python3 install.py --deps --tool=0.2.1 --ot=master`.


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

The authors would like to thank everyone who contributed to this project, including but not limited to 
- [Fabrice Benhamouda](http://www.normalesup.org/~fbenhamo/), 
- [Weikeng Chen](https://www.chenweikeng.com/), 
- [Shai Halevi](https://shaih.github.io/), 
- [Brett Hemenway](http://www.cis.upenn.edu/~fbrett/),
- [Zhicong Huang](https://acs6610987.github.io/), 
- [Wen-jie Lu](http://fionser.github.io/), 
- [Ivan Oliveira Nunes](https://sites.google.com/site/ivandeoliveiranunes/), 
- [David Cerezo Sánchez](http://cerezo.name/blog/about/), 
- [Phillipp Schoppmann](https://hu.berlin/schoppmp),
- [Chenkai Weng](https://github.com/carlweng),
- [Ruiyu Zhu](https://github.com/RuiyuZhu), 
- and others.


## Question
Please send emails to wangxiao@cs.northwestern.edu
