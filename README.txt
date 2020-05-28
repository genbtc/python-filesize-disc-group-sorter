#confirm python has the basic Pre-Requisities for "binpacking"
sudo apt-get install python3-pip
pip3 install setuptools wheel

# install "binpacking"
# documentation is @  https://pypi.org/project/binpacking/ (also installs numpy, future deps)
pip3 install binpacking
#It gets put into .local/bin , run the -h helpfile
~/.local/bin/binpacking -h 

#Edit my sizesort.py script to find your movie directory.
vim sizesort.py
# add weight,name to main file as a -H header (good seperation for later)
echo 'weight,name' > 4TB.csv
#Run the script to walk your filesystem. Gets the name and size of all files. append output using >> 
./sizesort.py >> 4TB.csv 

#Now run binpacking directly, give it some extra constraints, and send the STDOUT > to a "groups" list file
~/.local/bin/binpacking -f 4TB.csv -V 24159191040 -c 0 -l 700000000 -u 24159191040 -H > 4TB-groups.txt
# -f = source CSV file
# -H = header, acts as a seperator
# -V = maximum volume per bin = a 25GB BD-R Bluray is 24159191040 bytes accounting for ISO overhead (tune if you know otherwise)
# -c = 0, the column number where the weight is stored (keep this as is)
# -l = Lower bound 700MB (ignore files under this amount)
# -u = upper bound [same value as -V] (ignore files over this amount, or you will get invalid oversize bins)

#4TB-groups.txt
=== distributed items to bins with sizes ===
000 24087660456.0
001 24155201058.0
002 24060932900.0
003 24157094674.0
004 24141316858.0

#ls 4TB_*
4TB_000.csv
4TB_001.csv
4TB_002.csv
4TB_003.csv
4TB_004.csv

#Since it outputs multiple CSV files (1 per group) - to recombine them:
cat 4TB_* >> 4TB-regrouped.csv

#4TB-regrouped.csv
weight,name
23353336366.0,/home/genr8eofl/4TB/Movies/Int
734324090.0,/home/genr8eofl/4TB/Movies/Reven
weight,name
22515502123.0,/home/genr8eofl/4TB/Movies/2016
1639698935.0,/home/genr8eofl/4TB/Movies/2017 
weight,name
22415787323.0,/home/genr8eofl/4TB/Movies/2015
1645145577.0,/home/genr8eofl/4TB/Movies/H-WD5
weight,name
21523927037.0,/home/genr8eofl/4TB/Movies/2017
2633167637.0,/home/genr8eofl/4TB/Movies/2013 
weight,name
21293079365.0,/home/genr8eofl/4TB/Movies/2017
2848237493.0,/home/genr8eofl/4TB/Movies/2015 

#Now you know which combinations of files fit most optimally on 25GB bluray discs.
