import sys
import re
import os

# get the start directory
start = sys.argv[1]
# get the pattern from the command line arguments
pattern = sys.argv[2]
# convert them into regular expression
expr = re.compile(pattern)
# traverse the directories for all files
for root, dirs, files in os.walk(start):
    # if a file matches the pattern, print its name
    for fname in files:
        if expr.match(fname):
            print(os.path.join(root, fname))