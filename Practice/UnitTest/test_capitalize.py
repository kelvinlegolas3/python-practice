import unittest
from capitalize import capitalize_text

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = capitalize_text(text)
        self.assertEqual(result, 'Python')
    
    def test_multiple_words(self):
        text = 'kevin almario'
        result = capitalize_text(text)
        self.assertEqual(result, 'Kevin Almario')
        
if __name__ == '__main__':
    unittest.main()