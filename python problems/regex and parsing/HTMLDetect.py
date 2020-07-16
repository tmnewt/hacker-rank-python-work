# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

# there are 2 primary solutions. Using regex or using inbuilt HTMLparser.

from html.parser import HTMLParser

class DetectHTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a in attrs:
            print(f'-> {a[0]} > {a[1]}')

    def handle_endtag(self, tag):
        pass

fulltext = ''
for _ in range(int(input())):
    fulltext += input()

parser = DetectHTML()
parser.feed(fulltext)
parser.close