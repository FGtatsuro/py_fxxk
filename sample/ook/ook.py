#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from py_fxxk import BrainFxxk

class Ook(BrainFxxk):
    def __init__(self):
        BrainFxxk.__init__(self, ope={
            u'nxt':u'Ook. Ook? ',
            u'prv':u'Ook? Ook. ',
            u'inc':u'Ook. Ook. ',
            u'dec':u'Ook! Ook! ',
            u'put':u'Ook! Ook. ',
            u'get':u'Ook. Ook! ',
            u'opn':u'Ook! Ook? ',
            u'cls':u'Ook? Ook! ',
       })

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    Ook().fxxk(sys.argv[1])

if __name__ == '__main__':
    main()
