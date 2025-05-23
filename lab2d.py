#!/usr/bin/env python3

import sys

# Check for exactly 2 arguments (script name + 2 args = 3 total)
if len(sys.argv) != 3:
    print('Usage:', sys.argv[0], 'name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + age + ' years old.')
