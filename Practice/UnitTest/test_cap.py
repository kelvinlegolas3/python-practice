from unittest import TestCase
import cap

class TestCap(TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap