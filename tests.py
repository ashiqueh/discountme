import unittest
import tweets
import extract
import tags 

class TestMethods(unittest.TestCase):

	def test_get_codes(self):
		strings = ['use my discount code "ABC25" to get free stuff', 'check out this free deal with MYCODEHERE', 'check this discount "MYCODEHERE"', '', 'ab44ggre', '""']
		self.assertEqual(extract.get_codes(strings), ['ABC25', 'MYCODEHERE'])

if __name__ == '__main__':
    unittest.main()