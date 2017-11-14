# -*-coding:utf-8 -*-
# Author: guorch@buaa.edu.cn
# test_doubly_linked_list.py
from unittest import TestCase

# 2017/11/13 20:12
from doubly_linked_list_Problem7 import Frob, insert

class TestFrob(TestCase):
    def test_setBefore(self):
        '''
        andrew <- eric <- fred <- martha <- fred
        '''
        andrew = Frob('andrew')
        eric = Frob('eric')
        ruth = Frob('ruth')
        fred = Frob('fred')
        martha = Frob('martha')

        insert(eric, andrew)
        # andrew <- eric
        assert eric.getBefore().name == 'andrew'
        assert andrew.getAfter().name == 'eric'
        insert(eric, ruth)
        # andrew <- eric <- ruth
        assert eric.getAfter().name == 'ruth'
        assert ruth.getBefore().name == 'eric'
        insert(eric, fred)
        # andrew <- eric <- fred <- ruth
        assert eric.getAfter().name == 'fred'
        assert fred.getBefore().name == 'eric'
        assert fred.getAfter().name == 'ruth'
        assert ruth.getBefore().name == 'fred'
        insert(ruth, martha)
        # andrew <- eric <- fred <- martha <- ruth
        assert fred.getAfter().name == 'martha'
        assert martha.getBefore().name == 'fred'
        assert martha.getAfter().name == 'ruth'
        assert ruth.getBefore().name == 'martha'

    def multi_names(self):
        test_list = Frob('zsa zsa')
        a = Frob('ashley')
        m = Frob('marcella')
        v = Frob('victor')
        insert(test_list, m)
        assert m.getAfter().name == 'zsa zsa'
        assert test_list.getBefore().name == 'marcella'
        'marcella, zsa zsa'
        insert(m, a)

        insert(a, v)
        assert a.getAfter().name == 'marcella'
        assert v.getBefore().name == 'marcella'
        assert m.getAfter().name == 'victor'
        assert v.getAfter().name == 'zsa zsa'
        assert test_list.getBefore().name == 'victor'

    def multi_names2(self):
        test_list = Frob('mark')
        c = Frob('craig')
        insert(test_list, Frob("sam"))
        assert test_list.getAfter().name == 'sam'
        insert(test_list, Frob("nick"))
        assert test_list.getAfter().name == 'nick'
        assert test_list.getAfter().getAfter().name == 'sam'
        insert(test_list, c)
        assert test_list.getBefore().name == 'craig'
        insert(c, Frob("xanthi"))
        'craig mark nick sam xanthi'
        assert test_list.getAfter().getAfter().getAfter().name == 'xanthi'
        insert(test_list, Frob("jayne"))
        'craig jayne mark nick sam xanthi'
        assert c.getAfter().name == 'jayne'
