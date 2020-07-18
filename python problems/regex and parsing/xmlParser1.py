# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem

import xml.etree.ElementTree as etree
import os

def get_attr_number(node):
    count = 0
    for elm in node.iter():
        count += len(elm.attrib)
    
    return count


os.chdir('python problems\\regex and parsing')
tree = etree.parse('country_data.xml')
root = tree.getroot()
#print(root)
#print(root.tag)
#print('type:', type(root.tag))
#print(root.attrib)
#print('type:', type(root.attrib))
#for child in root:
#    print(child.tag, child.attrib)

count = 0
for elm in root.iter():
    if len(elm.attrib) != 0:
        count += len(elm.attrib)
        print(elm.attrib)
print(count)