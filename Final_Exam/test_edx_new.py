# -*-coding:utf-8 -*-
# Author: guorch@buaa.edu.cn
# test_edx_new.py
# 2017/11/14 18:50

import unittest
from CourceInfo_Final_Exam_P5 import * # edx, courseInfo

class TestEdx(unittest.TestCase):
    def test_edx(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        self.assertEqual([e.courseName for e in edX.myCourses], [courseInfo("6.00x").courseName, courseInfo("6.01x").courseName, courseInfo("6.02x").courseName])

    def test_setGrade(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        self.assertEqual(edX.myCourses[0].getGrade(), "No Grade")
        self.assertEqual( edX.myCourses[1].getGrade(), "No Grade")
        self.assertEqual(edX.myCourses[2].getGrade(), "No Grade")

        edX.setGrade(100, "6.00x")
        edX.setGrade(90, "6.01x")
        edX.setGrade(80, "6.02x")
        self.assertEqual(edX.myCourses[0].getGrade(), 100)
        self.assertEqual(edX.myCourses[1].getGrade(), 90)
        self.assertEqual(edX.myCourses[2].getGrade(), 80)
        self.assertEqual(edX.getGrade("6.00x"), 100)
        self.assertEqual(edX.getGrade("6.01x"), 90)
        self.assertEqual(edX.getGrade("6.02x"), 80)
        edX.setGrade(50)
        self.assertEqual(edX.getGrade("6.00x"), 100)
        self.assertEqual(edX.getGrade("6.01x"), 90)
        self.assertEqual(edX.getGrade("6.02x"), 80)
        self.assertEqual(edX.getGrade(), 80)

    def test_getGrade(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        edX.setGrade(100, "2.01x")
        self.assertEqual(edX.getGrade("2.01x"), -1)

    def test_setPset(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        edX.setPset(2, 100, "6.02x")
        edX.setPset(2, 90, "6.02x")
        edX.setPset(3, 95, "6.02x")
        self.assertEqual(edX.getPset(2, "6.02x"), 100)
        self.assertEqual(edX.getPset(3, "6.02x"), 95)
        self.assertEqual(edX.getPset(4, "6.02x"), None)
        edX.setPset(4, 100)
        self.assertEqual(edX.getPset(4), 100)

    def test_getPset(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        edX.setPset(2, 100,"6.02x")
        edX.setPset(2, 100,"2.01x")
        self.assertEqual(edX.getPset(2, "6.02x"), 100)
        self.assertEqual(edX.getPset(3, "6.02x"), None)
        self.assertEqual(edX.getPset(2, "2.01x"), -1)

if __name__ == '__main__':
    unittest.main()
