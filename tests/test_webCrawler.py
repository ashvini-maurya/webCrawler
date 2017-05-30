from nose.tools import *
from webCrawler.webCrawler.webCrawler import WebCrawler
import unittest

class TestForWebCrawler(unittest.TestCase):
	
	def setUp(self):
		self.webc = WebCrawler()

	def test_web_crawler_with_keyword(self):
		result = self.webc.web_crawler_query1('boys')
		self.assertEqual(1500, int(result))

	def test_web_crawler_with_keyword_and_page_number(self):
		result = self.webc.web_crawler_query2('boys', str(20))
		self.assertEqual(40, int(result))

	def test_web_crawler_with_keyword_does_not_exist(self):
		result = self.webc.web_crawler_query1('ashvini')
		self.assertRaises(result, msg='Keyword - ashvini, does not exist!')
	
	def test_web_crawler_with_keyword_existing_but_page_does_not_exist(self):
		result = self.webc.web_crawler_query2('boys', str(68))
		self.assertRaises(result, msg='There are no matches for your selection')
		
	

if __name__ == '__main__':
	unittest.main()
