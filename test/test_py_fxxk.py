#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose import tools
from py_fxxk import BrainFxxk

class test_bf(object):

    def test_init(self):
        bf = BrainFxxk()
        tools.eq_(0, bf.ptr)        
        tools.eq_(0, bf.cur)
        tools.assert_true(hasattr(bf, u'ope'))
        tools.eq_(u'>', bf.ope[u'nxt'])
        tools.eq_(30000, len(bf.buf))
        [tools.eq_(0, val) for val in bf.buf]

    def test_set_ope(self):
        bf = BrainFxxk({u'nxt':u'test'})
        tools.eq_(0, bf.ptr)        
        tools.eq_(0, bf.cur)
        tools.assert_true(hasattr(bf, u'ope'))
        tools.eq_(u'test', bf.ope[u'nxt'])
        tools.eq_(30000, len(bf.buf))
        [tools.eq_(0, val) for val in bf.buf]

    def test_nxt(self):
        bf = BrainFxxk()
        bf.nxt()
        tools.eq_(1, bf.ptr)        
    
    def test_prv(self):
        bf = BrainFxxk()
        bf.prv()
        tools.eq_(-1, bf.ptr)        
    
    def test_inc(self):
        bf = BrainFxxk()
        bf.inc()
        tools.eq_(1, bf.buf[0])        
    
    def test_dec(self):
        bf = BrainFxxk()
        bf.dec()
        tools.eq_(-1, bf.buf[0])        
    
    def test_opn(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.src = u'[>>>>++]>>'        
        bf.opn()
        tools.eq_(7, bf.cur)

    def test_opn_nest(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.src = u'[->[->>+<<]>>[-<+<+>>]<<<]<'
        bf.ptr = 0

        # buf[ptr] = 0
        bf.buf[bf.ptr] = 0
        # out
        bf.cur = 0
        bf.opn()
        tools.eq_(25, bf.cur)
        # in1
        bf.cur = 3
        bf.opn()
        tools.eq_(10, bf.cur)
        # in2
        bf.cur = 13
        bf.opn()
        tools.eq_(21, bf.cur)

        # ptr = 1
        bf.buf[bf.ptr] = 1
        # out
        bf.cur = 0
        bf.opn()
        tools.eq_(0, bf.cur)
        # in1
        bf.cur = 3
        bf.opn()
        tools.eq_(3, bf.cur)
        # in2
        bf.cur = 13
        bf.opn()
        tools.eq_(13, bf.cur)
    
    def test_cls(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.src = u'[>>>>++]>>'
        bf.cur = 7        
        bf.ptr = 0
        bf.buf[0] = 2
        bf.cls()
        tools.eq_(0, bf.cur)

    def test_cls_nest(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.src = u'[->[->>+<<]>>[-<+<+>>]<<<]<'
        bf.ptr = 0

        # ptr = 0
        bf.buf[bf.ptr] = 0
        # out
        bf.cur = 25
        bf.cls()
        tools.eq_(25, bf.cur)
        # in1
        bf.cur = 10
        bf.cls()
        tools.eq_(10, bf.cur)
        # in2
        bf.cur = 21
        bf.cls()
        tools.eq_(21, bf.cur)

        # ptr = 1
        bf.buf[bf.ptr] = 1
        # out
        bf.cur = 25
        bf.cls()
        tools.eq_(0, bf.cur)
        # in1
        bf.cur = 10
        bf.cls()
        tools.eq_(3, bf.cur)
        # in2
        bf.cur = 21
        bf.cls()
        tools.eq_(13, bf.cur)

    def test_compile(self):
        test_ope = {
            u'nxt':u'a',
            u'prv':u'b',
            u'inc':u'c',
            u'dec':u'd',
            u'put':u'e',
            u'get':u'f',
            u'opn':u'g',
            u'cls':u'h',
        }
        bf = BrainFxxk(test_ope)
        src = bf._compile('gaaaacchaa')
        tools.eq_(u'[>>>>++]>>', src)

    def test_compile_multiple(self):
        test_ope = {
            u'nxt':u'a',
            u'prv':u'b',
            u'inc':u'c',
            u'dec':u'd',
            u'put':u'e',
            u'get':u'f',
            u'opn':u'あい',
            u'cls':u'h',
        }
        bf = BrainFxxk(test_ope)
        src = bf._compile('あいaaaacchaa')
        tools.eq_(u'[>>>>++]>>', src)

    def test_compile_special_chars(self):
        test_ope = {
            u'nxt':u'a',
            u'prv':u'b',
            u'inc':u'c',
            u'dec':u'd',
            u'put':u'e',
            u'get':u'f',
            u'opn':u'[*]',
            u'cls':u'[*',
        }
        bf = BrainFxxk(test_ope)
        src = bf._compile('[*]aaaacc[*aa')
        tools.eq_(u'[>>>>++]>>', src)

    def test_fxxk(self):
        bf = BrainFxxk()
        bf.fxxk(u'>>>>++>>')
        tools.eq_(2, bf.buf[4])
        tools.eq_(6, bf.ptr)

