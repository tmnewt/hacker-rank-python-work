# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem?h_r=next-challenge&h_v=zen
import os
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(root, level):
    global maxdepth
    if (level >= maxdepth): 
        maxdepth += 1
    for elm in root: 
        depth(elm, level+1)


os.chdir('python problems\\regex and parsing')
tree = etree.parse('country_data.xml')
myroot = tree.getroot()

depth(myroot, -1)
print(maxdepth)




