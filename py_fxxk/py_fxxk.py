#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

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

    def __init__(self, ope={}, encode=u'utf-8', debug=True):
        self.ptr = 0
        self.cur = 0
        self.buf = [0] * 30000
        self.src = u''
        self.encode = encode
        self.debug = debug
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

    def nxt(self):
        self.ptr += 1
        if self.debug:
            print 'ptr:{0} -> {1}'.format(self.ptr - 1, self.ptr)

    def prv(self):
        self.ptr -= 1
        if self.debug:
            print 'ptr:{0} -> {1}'.format(self.ptr + 1, self.ptr)

    def inc(self):
        self.buf[self.ptr] += 1
        if self.debug:
            print self.buf[:11],'cur:{0},ptr:{1}'.format(self.cur,self.ptr)

    def dec(self):
        self.buf[self.ptr] -= 1
        if self.debug:
            print self.buf[:11],'cur:{0},ptr:{1}'.format(self.cur,self.ptr)

    def put(self):
        sys.stdout.write(chr(self.buf[self.ptr]))

    def get(self):
        self.buf[self.ptr] = ord(sys.stdin.read(1))

    def opn(self):
        if self.buf[self.ptr] != 0:
            return
        _cur = self.cur
        self.cur = (
                self._find_correspondence(
                    self.src, 
                    _cur, 
                    self.default_ope[u'opn'], 
                    self.default_ope[u'cls']) 
                + 1)
        if self.debug:
            print 'opn_cur:{0} -> cls_cur:{1} ptr:{2}'.format(_cur, self.cur - 1, self.ptr)

    def cls(self):
        if self.buf[self.ptr] == 0:
            return
        _src = ''.join([s for s in reversed(self.src)])
        _cur = len(_src) -1 - self.cur
        self.cur = (
                len(_src) - 1 -
                self._find_correspondence(
                    _src, 
                    _cur, 
                    self.default_ope[u'cls'], 
                    self.default_ope[u'opn'])
                )
        if self.debug:
            print 'cls_cur:{0} -> opn_cur:{1} by ptr:{2}'.format(len(_src) -1 - _cur, self.cur, self.ptr)

    def _find_correspondence(self, src, cur, start_code, end_code):
        end_num = 1
        while end_num > 0:
            start_pos = src.find(start_code, cur + 1)
            end_pos = src.find(end_code, cur + 1)
            if end_pos == -1:
                raise Exception("Syntax Error: Not Found '{0}' operation".format(end_code))
            if start_pos == -1 or end_pos < start_pos:
                cur = end_pos
                end_num -= 1
                continue
            cur = start_pos
            end_num += 1
        return cur
            
