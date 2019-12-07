#! /usr/bin/python

import unittest
import mojprogram

class TestTDD1(unittest.TestCase):#clasa
    def test_zwroc_100(self):
        wynik=mojprogram.zwroc_100()#zmienna zroc_100 z mojegoprogramu
        self.assertEqual(wynik,100)#self bo dla ciala klasy aasercjA porownujemy zmienna wynik do wartosci 100

    def test_zwroc_parametr(self):
        a=22
        wynik=mojprogram.zwroc_parametr(22)
        self.assertEqual(wynik,22)
        #albo od odrazu
        #self.assertEqual(mojprogram.test_zwroc_parametr(124),124)

if __name__=="__main__":
    unittest.main()
