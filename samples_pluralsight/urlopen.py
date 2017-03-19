#!/usr/bin/env python3
##### the line above will make the script executable from command line like: ./urlopen http://etc.com
import sys
from urllib.request import urlopen

# opens a txt from a url and return his words in a list
def getWords(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


# prints each item of a list
def print_items(items):
    for item in items:
        print(item)


# main function
def main(url='http://sixty-north.com/c/t.txt'):
    words = getWords(url)
    print_items(words)


""" __name__ can be the module name, in this case "urlopen" if
# called directly from python interpreter, eg: >>> import urlopen
#                       OR
# can be "__main__" if called directly from OS command line like a script, eg: $ python3 urlopen.py """

# to ensure that the function will be called when executing from OS command line,
# this is a good idea when you don't want the module execute the function, just when
# called directly from OS command line, eg: $ python3 urlopen.py
if __name__ == '__main__':
    main(sys.argv[1])   # sys.argv[1] is the parameter passed from
                        # OS command line eg: $ python3 urlopen.py http://etc.com