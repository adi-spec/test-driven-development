#! /usr/bin/python

import unittest
import kalkulator

class TestTDD2(unittest.TestCase):
    def test_dodawanie(self):
        a=1
        b=1
        self.assertEqual(kalkulator.dodawanie(1,1),2)

    def test_odejmowanie(self):
        self.assertEqual(kalkulator.odejmowanie(2,1),1)

if __name__=="__main__":
    unittest.main()
