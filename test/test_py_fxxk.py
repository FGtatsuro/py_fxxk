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
    
    def test_put(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.buf[0] = 72       
        bf.put()
        tools.eq_(u'H', bf.out[0])

    def test_get(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.src = u'a'       
        bf.get()
    
    def test_opn(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.src = u'[>>>>++]>>'        
        bf.opn()
        tools.eq_(8, bf.cur)
    
    def test_cls(self):
        bf = BrainFxxk()
        # for test, insert data
        bf.src = u'[>>>>++]>>'
        bf.cur = 7        
        bf.ptr = 0
        bf.buf[0] = 2
        bf.cls()
        tools.eq_(0, bf.cur)

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

