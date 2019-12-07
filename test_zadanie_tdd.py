#! /usr/bin/python

import unittest
import zadanie_tdd

class TestTDD(unittest.TestCase):
    def test_lenght_ciagu(self):
        self.assertEqual(lenght_ciagu('12345'),5)

    def test_lower_ciagu(self):
        self.assertEqual(lower_ciagu('TEST'),'test')

    def test_upper_ciagu(self):
        self.assertEqual(upper_ciagu('test'),'TEST')

    def test_capitalize_ciagu(self):
        self.assertEqual(capitalize_ciagu('test'),'Test')

    def test_index_ciagu(self):
        self.assertEqual(index_ciagu('test'),0)

if __name__=="__main__":
    unittest.main()
