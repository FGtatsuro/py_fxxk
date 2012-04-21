#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class BrainFxxk(object):

    default_ope = {
        u'nxt':u'>',
        u'prv':u'<',
        u'inc':u'+',
        u'dec':u'-',
        u'put':u'.',
        u'get':u',',
        u'opn':u'[',
        u'cls':u']',
    }

    def __init__(self, ope={}, encode=u'utf-8'):
        self.ptr = 0
        self.cur = 0
        self.buf = [0] * 30000
        self.src = u''
        self.out = []
        self.encode = encode
        self.set_ope(ope)

    def _unicode(self, src, encode):
        if type(src) is str:
            return unicode(src, encode)
        return src

    def _compile(self, src):
        invert = dict((v, k) for k, v in self.ope.iteritems())
        keys = [re.escape(k) for k in invert.keys()]
        keys.sort(cmp=(lambda x, y: len(y) - len(x)))
        regex = re.compile('|'.join(keys))
        uni_src = self._unicode(src, self.encode)
        uni_src = regex.sub((lambda m: BrainFxxk.default_ope[invert[m.group(0)]]), uni_src)
        return uni_src

    def set_ope(self, ope):
        self.ope = BrainFxxk.default_ope.copy()
        for k in ope:
            if not k in self.ope:
                continue
            self.ope[k] = self._unicode(ope[k], self.encode)

    def fxxk(self, src):
        self.__init__()
        try:
            with open(src) as f:
                src = f.read()
        except IOError:
            print "fxxk regards 'src' as not file, but str."
        self.src = self._compile(self._unicode(src.strip(), self.encode))
        invert = dict((v, k) for k, v in BrainFxxk.default_ope.iteritems())
        while self.cur < len(self.src):
            ope = self.src[self.cur]
            try:
                getattr(self, invert[ope])()
            except:
                pass
            self.cur += 1
        print ''.join(self.out).encode(self.encode)

    def nxt(self):
        self.ptr += 1

    def prv(self):
        self.ptr -= 1

    def inc(self):
        self.buf[self.ptr] += 1

    def dec(self):
        self.buf[self.ptr] -= 1

    def put(self):
        self.out.append(chr(self.buf[self.ptr]))

    def get(self):
        self.buf[self.ptr] = self.src[self.cur]

    def opn(self):
        if self.buf[self.ptr] == 0:
            self.cur = self.src.index(self.default_ope[u'cls'], self.cur) + 1

    def cls(self):
        if self.buf[self.ptr] != 0:
            self.cur = self.src.rindex(self.default_ope[u'opn'], 0, self.cur)
