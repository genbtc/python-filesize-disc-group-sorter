git config --global user.email "genBTC@gmx.com"
git init
git add sizesort.py && git commit

./sizesort.py > Hmovies.csv

#pre-requisities for binpacking
sudo apt-get install python3-pip
pip3 install setuptools wheel
# need https://pypi.org/project/binpacking/ (also installs numpy, future,)
pip3 install binpacking
~/.local/bin/binpacking -h 
~/.local/bin/binpacking -f Hmovies.csv -V 24159191040 -c 0

./sizesort.py > 4TB.csv 
# + add weight,name to main file -H header, and act as a seperator. Lower bound 700MB, upper bound = maxbinsize
~/.local/bin/binpacking -f 4TB.csv -V 24159191040 -c 0 -l 700000000 -u 24159191040 -H > 4TB-groups.txt
cat 4TB_* >> 4TB-grouped.csv

