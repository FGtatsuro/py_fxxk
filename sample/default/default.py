#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from py_fxxk import BrainFxxk

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    BrainFxxk(debug=False).fxxk(sys.argv[1])

if __name__ == '__main__':
    main()
