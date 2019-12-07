import unittest
import zadanie_tdd


class TestTDD(unittest.TestCase):
    def test_lenght_ciagu(self):
        self.assertEqual(zadanie_tdd.length_ciagu('12345'),5)

    def test_lower_ciagu(self):
        self.assertEqual(zadanie_tdd.lower_ciagu('TEST'),'test')

    def test_upper_ciagu(self):
        self.assertEqual(zadanie_tdd.upper_ciagu('test'),'TEST')

    def test_capitalize_ciagu(self):
        self.assertEqual(zadanie_tdd.capitalize_ciagu('test'),'Test')

    def test_index_ciagu(self):
        self.assertEqual(zadanie_tdd.index_ciagu('test', 'test parameter'), 0)


if __name__ == "__main__":
    unittest.main()