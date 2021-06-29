from text_tools import to_upper, to_word_list_isupper
import unittest

class TestStringMethods(unittest.TestCase):
    #test1
    def test_upper(self):
        self.assertEqual(to_upper('foo'), 'FOO')

    # test2 
    # test with message 
    def test_word_list_isupper1(self):
        self.assertTrue(to_word_list_isupper(['i', 'LOVE', 'PYTHON' ]), "test 2 return False value instead of True")

    # test3 
    def test_word_list_isupper2(self):
        self.assertTrue(to_word_list_isupper())

    # test4 
    def test_word_list_isupper3(self):
        self.assertTrue(to_word_list_isupper("I LOVE YOU"))

    # test5 
    def test_word_list_isupper3(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper("I LOVE YOU")

    # test6    
    def test_word_list_isupper4(self):
        self.assertFalse(to_word_list_isupper(['i', 'LOVE', 'PYTHON' ]))


if __name__ == '__main__':
    unittest.main()