import sys
import re
import os

# get the pattern from the command line arguments
pattern = sys.argv[1]
# convert them into regular expression
expr = re.compile(pattern)
# traverse the directories for all files
for root, dirs, files in os.walk('h:/Playground/'):
    # if a file matches the pattern, print its name
    for fname in files:
        if expr.search(fname):
            print(os.path.join(root, fname))