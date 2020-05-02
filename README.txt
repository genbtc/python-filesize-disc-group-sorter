git config --global user.email "genBTC@gmx.com"
git init
git add sizesort.py && git commit

./sizesort.py > Hmovies.csv

sudo apt-get install python3-pip
pip3 install setuptools wheel
# https://pypi.org/project/binpacking/
pip3 install binpacking
/home/genr8eofl/.local/bin/binpacking -h 
/home/genr8eofl/.local/bin/binpacking -f Hmovies.csv -V 24159191040 -c 0 -H
