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
        assert martha.getAfter().name == 'fred'
        assert ruth.getBefore().name == 'martha'
