#!/usr/bin/env python3

import quine
import sys

source = quine.generate()

if len(sys.argv) == 1:
    print(source, end="")
elif len(sys.argv) == 2:
    with open(sys.argv[1], "w") as outfile:
        outfile.write(source)
else:
    print("Call without parameter to write to stdout or with a filename to write to.")


