# Author: guorch@buaa.edu.cn
# test_edx.py
from unittest import TestCase

# 2017/11/12 16:16
from CourceInfo_Final_Exam_P5 import edx, courseInfo

class TestEdx(TestCase):
    def test_edx(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        assert edX.myCourses == [courseInfo("6.00x"), courseInfo("6.01x"), courseInfo("6.02x")]

    def test_setGrade(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        print [e.grade for e in edX.myCourses]

        # edX.setGrade(100, "6.00x")
        for c in edX.myCourses:
            if c.grade == "No Grade":
                c.grade = 100
        print [e.grade for e in edX.myCourses]
        assert courseInfo("6.00x").getGrade() == "No Grade"
        # edX.setGrade(90, "6.01x")
        # edX.setGrade(80, "6.02x")
    #
    # def test_getGrade(self):
    #     edX.getGrade("6.00x")
    #     edX.getGrade("6.01x")
    #     edX.getGrade("6.02x")
    #
    # def test_setPset(self):
    #     edX.setPset(2, 100, "6.02x")
    #     edX.setPset(2, 90, "6.02x")
    #     edX.setPset(3, 95, "6.02x")
    #
    # def test_getPset(self):
    #     edX.getPset(2, "6.02x")
    #     edX.getPset(3, "6.02x")
    #     edX.getPset(4)
