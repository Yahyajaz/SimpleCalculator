from Calculator import Calculator
import pytest
import unittest


class test_PythonSimpleCalc(unittest.TestCase):
    def test_calc(self):
        c = Calculator()
        assert c

    def test_calc_add(self):
        c = Calculator()
        assert c.add(3, 2) == 5

    def test_calc_subtract(self):
        c = Calculator()
        assert c.subtract(0, 10) == -10

    def test_calc_multiply(self):
        c = Calculator()
        assert c.multiply(2, 2) == 4

    def test_calc_divide(self):
        c = Calculator()
        assert c.divide(10, 5) == 2

    def test_calc_square(self):
        c = Calculator()
        assert c.square(10) == 100

    def test_calc_squareroot(self):
        c = Calculator()
        assert c.squareroot(9) == 3
