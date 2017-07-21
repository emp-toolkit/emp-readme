git clone https://github.com/emp-toolkit/emp-readme.git
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
bash $DIR/install_packages.sh
bash $DIR/install_relic.sh
bash $DIR/install_emp-tool.sh
bash $DIR/install_emp-ot.sh
bash $DIR/install_emp-m2pc.sh
bash $DIR/install_emp-sh2pc.sh
