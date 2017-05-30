import urllib2
from bs4 import BeautifulSoup
import re



def web_crawler_query1(keyword):
	#keyword = raw_input("please enter keyword: ")
	page = urllib2.urlopen('http://shopping.com/products?KW=' + str(keyword)).read()
	soup = BeautifulSoup(page, "lxml")
	paginated = list(soup.findAll('a', attrs={'name': re.compile(r"^PL")}))
	if paginated == []:
		c1 = len(list(soup.findAll('div', attrs={'id': re.compile(r"^quickLookItem-")})))
		#print "Total results for " + keyword + ": " + str(c1)
		return str(c1)
	else:
    		soup = BeautifulSoup(str(paginated[-2]), "lxml")
    		anchor = soup.findAll('a', href=True)
    		page = urllib2.urlopen('http://shopping.com'+anchor[0]['href'])
    		soup = BeautifulSoup(page, "lxml")
    		c1 = len(list(soup.findAll('div', attrs={'id': re.compile(r"^quickLookItem-")})))
    		count = list(soup.find('span', attrs={'class': 'numTotalResults'}))
    		arr = count[0].split()
    		arr[1] = arr[1].replace(',','')
    		#print "Total results for " + keyword + ": " + str(int(arr[1])+c1-1)

	return str(int(arr[1])+c1-1)
	#	print 
	#	print "***Query 2***"
	#	print
		# Query 2

def web_crawler_query2(keyword2, page_number):
	#keyword2 = raw_input("Please enter keyword: ")
	#page_number = raw_input("please enter page number: ")
	page2 = urllib2.urlopen('http://www.shopping.com/products~PG-' + page_number + '?KW=' + str(keyword2)).read()
	soup = BeautifulSoup(page2, "lxml")
	paginated_ = list(soup.findAll('a', attrs={'name': re.compile(r"^PL")}))
	c2 = len(list(soup.findAll('div', attrs={'id': re.compile(r"^quickLookItem-")})))
	#print "Total results for " + keyword2 + " on page number " + page_number + ": " + str(c2)
	return str(c2)
		

result1 = web_crawler_query1('boys')
result2 = web_crawler_query2('boys', str(2))
print result1
print result2
