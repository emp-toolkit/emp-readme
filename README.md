# EMP Toolkit Readme Page
<img src="https://raw.githubusercontent.com/emp-toolkit/emp-readme/master/art/logo-full.jpg" width=300px/>

## Installation

1. Go the the folder you want to install everything

2. `curl https://raw.githubusercontent.com/emp-toolkit/emp-readme/master/scripts/install.py -O`

3. `python install.py --deps --tool --ot` to install code dependency, and master branch of emp-tool and emp-ot. More flags can be added including `--sh2pc`, `--ag2pc`, `--agmpc`, `--zk`.
- You can also install a branch using `python install.py --[repo1]=[branch1] --[repo2]=[branch2]`, e.g., `python install.py --deps --tool=0.2.1 --ot=master`


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
