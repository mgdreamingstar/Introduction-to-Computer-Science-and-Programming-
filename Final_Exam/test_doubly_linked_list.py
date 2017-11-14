# -*-coding:utf-8 -*-
# Author: guorch@buaa.edu.cn
# test_doubly_linked_list.py
from unittest import TestCase

# 2017/11/13 20:12
from doubly_linked_list_Problem7 import Frob, insert, walk_through

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
        self.assertEqual(eric.getBefore().name, 'andrew')
        self.assertEqual(andrew.getAfter().name, 'eric')
        insert(eric, ruth)
        # andrew <- eric <- ruth
        self.assertEqual(eric.getAfter().name, 'ruth')
        self.assertEqual(ruth.getBefore().name, 'eric')
        insert(eric, fred)
        # andrew <- eric <- fred <- ruth
        self.assertEqual(eric.getAfter().name, 'fred')
        self.assertEqual(fred.getBefore().name, 'eric')
        self.assertEqual(fred.getAfter().name, 'ruth')
        self.assertEqual(ruth.getBefore().name, 'fred')
        insert(ruth, martha)
        # andrew <- eric <- fred <- martha <- ruth
        self.assertEqual(fred.getAfter().name, 'martha')
        self.assertEqual(martha.getBefore().name, 'fred')
        self.assertEqual(martha.getAfter().name, 'ruth')
        self.assertEqual(ruth.getBefore().name, 'martha')
        # walk_through
        self.assertEqual(walk_through(eric), ['andrew', 'eric', 'fred', 'martha', 'ruth'])

    def test_multi_names(self):
        test_list = Frob('zsa zsa')
        a = Frob('ashley')
        m = Frob('marcella')
        v = Frob('victor')
        insert(test_list, m)
        self.assertEqual(m.getAfter().name, 'zsa zsa')
        self.assertEqual(test_list.getBefore().name, 'marcella')
        'marcella, zsa zsa'
        insert(m, a)

        insert(a, v)
        self.assertEqual(a.getAfter().name, 'marcella')
        self.assertEqual(v.getBefore().name, 'marcella')
        self.assertEqual(m.getAfter().name, 'victor')
        self.assertEqual(v.getAfter().name, 'zsa zsa')
        self.assertEqual(test_list.getBefore().name, 'victor')

        # walk through
        self.assertEqual(walk_through(test_list), ['ashley', 'marcella', 'victor', 'zsa zsa'])

    def test_multi_names2(self):
        test_list = Frob('mark')
        c = Frob('craig')
        insert(test_list, Frob("sam"))
        self.assertEqual(test_list.getAfter().name, 'sam')
        insert(test_list, Frob("nick"))
        self.assertEqual(test_list.getAfter().name, 'nick')
        self.assertEqual(test_list.getAfter().getAfter().name, 'sam')
        insert(test_list, c)
        self.assertEqual(test_list.getBefore().name, 'craig')
        insert(c, Frob("xanthi"))
        'craig mark nick sam xanthi'
        self.assertEqual(test_list.getAfter().getAfter().getAfter().name, 'xanthi')
        insert(test_list, Frob("jayne"))
        'craig jayne mark nick sam xanthi'
        self.assertEqual(c.getAfter().name, 'jayne')

    def test_multi_names3(self):
        test_list = Frob('eric')
        insert(test_list, Frob("eric"))
        insert(test_list, Frob("chris"))
        insert(test_list, Frob("john"))
        insert(test_list, Frob("john"))
        insert(test_list, Frob("chris"))
        insert(test_list, Frob("eric"))
        insert(test_list, Frob("john"))
        insert(test_list, Frob("chris"))

        self.assertEqual(walk_through(test_list), ['chris', 'chris', 'chris', 'eric', 'eric', 'eric', 'john', 'john', 'john'])

if __name__ == '__main__':
    unittest.main()
