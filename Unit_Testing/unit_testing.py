# unit testing is a technique used for testing a block of code with different paramater.

# Arrange -> set up data set
# Act -> Execute peace of code with the prepared data set
# Assert -> comparing expected and actual result


# You developed one test case -> Login functionality -> Multiple combinantion of data

# get locator of url
# enter username -> combination of username-> valid/invalue -> leng should not 20 charact ->
# enter password -> valid/invalid
# click on login


import unittest
import re
def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b


class TestCase1(unittest.TestCase):
    def test1(self):
        self.assertEqual(addition(10,20),30)

    def test2(self):
        self.assertEqual(addition(20,30),50)

    def test3(self):
        self.assertEqual(subtraction(20, 30), 30)


