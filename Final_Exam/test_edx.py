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
        assert edX.myCourses[0].getGrade() == "No Grade"
        assert edX.myCourses[1].getGrade() == "No Grade"
        assert edX.myCourses[2].getGrade() == "No Grade"

        edX.setGrade(100, "6.00x")
        edX.setGrade(90, "6.01x")
        edX.setGrade(80, "6.02x")
        assert edX.myCourses[0].getGrade() == 100
        assert edX.myCourses[1].getGrade() == 90
        assert edX.myCourses[2].getGrade() == 80
        assert edX.getGrade("6.00x") == 100
        assert edX.getGrade("6.01x") == 90
        assert edX.getGrade("6.02x") == 80
        edX.setGrade(50)
        assert edX.getGrade("6.00x") == 100
        assert edX.getGrade("6.01x") == 90
        assert edX.getGrade("6.02x") == 80
        assert edX.getGrade() == 80

    def test_getGrade(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        edX.setGrade(100, "2.01x")
        assert edX.getGrade("2.01x") == -1

    def test_setPset(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        edX.setPset(2, 100, "6.02x")
        edX.setPset(2, 90, "6.02x")
        edX.setPset(3, 95, "6.02x")
        assert edX.getPset(2, "6.02x") == 100
        assert edX.getPset(3, "6.02x") == 95
        assert edX.getPset(4, "6.02x") == None
        edX.setPset(4, 100)
        assert edX.getPset(4) == 100

    def test_getPset(self):
        edX = edx(["6.00x", "6.01x", "6.02x"])
        edX.setPset(2, 100,"6.02x")
        edX.setPset(2, 100,"2.01x")
        assert edX.getPset(2, "6.02x") == 100
        assert edX.getPset(3, "6.02x") == None
        assert edX.getPset(2, "2.01x") == -1
