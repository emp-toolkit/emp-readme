# EMP Toolkit Readme Page
<img src="https://raw.githubusercontent.com/emp-toolkit/emp-readme/main/art/logo-full.jpg" width=300px/>

> **Which version do I want?**
>
> - **Existing projects pinned to a published release: stay on `v0.3.x`** —
>   `python3 install.py --tool=v0.3.x --ot=v0.3.x --sh2pc=v0.3.x`
>   reproduces the prior emp-toolkit line. Bug fixes and security
>   patches will be backported to `v0.3.x`.
> - **New projects, or willing to migrate: track `main`** — the default
>   for `--tool` / `--ot` / `--sh2pc`. It will become `1.0.0-alpha`
>   after a polish pass and then `1.0.0`. Faster, cleaner APIs, but
>   the API is not yet frozen and headers may move between alphas.
>
> The remaining flags (`--zk`, `--ag2pc`, `--agmpc`) still default to
> `master` — those repos haven't migrated yet.

## Installation

Requires CMake 3.21+ (Ubuntu 22.04+, recent macOS) and Python 3.

1. Go to the folder you want to install everything

2. `curl https://raw.githubusercontent.com/emp-toolkit/emp-readme/main/scripts/install.py -O`

3. `python3 install.py --deps --tool --ot` to install dependencies, plus the `main` branch of `emp-tool` and `emp-ot`. More flags can be added including `--sh2pc`, `--ag2pc`, `--agmpc`, `--zk`.
- You can also install a specific branch using `python3 install.py --[repo1]=[branch1] --[repo2]=[branch2]`, e.g., `python3 install.py --deps --tool=v0.3.x --ot=v0.3.x`.


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
