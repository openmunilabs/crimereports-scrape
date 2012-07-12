

#return feed object
def get_feed(lang):
	if lang=='english':
		return feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
	return feedparser.parse('http://www.bbc.co.uk/'+lang+'/index.xml')


#return list of articles
def get_articles(lang):
	feed=get_feed(lang)
	links=[]
	for entry in feed.entries:
		#print entry['title']
		#print entry['link']
		links.append(entry['link'])

	return links

def get_article(url):
	print "-----------------------------------"
	print url
	doc = parse(url).getroot()
	try:
		body=doc.cssselect('div.story-body')[0]
		print body.text_content()
	except:
		print 'no story-body'


import feedparser
import urllib

from lxml.html import parse

home='http://news.arlingtonva.us'

home_url='http://news.arlingtonva.us/pr/ava/'
crime_home="crime-reports.aspx"

links={}
crimes={}

def crawl(path):
	print "crawling: ",path
	url=home_url+path
	
	doc=parse(url).getroot()
	ll=doc.cssselect('div.prPaging div a')

	for l in ll:
		link=l.attrib['href']
		if link not in links.keys():
			links[link]={"status":"new"}
			crawl(link)
		else:
			links[link]={"status":"done"}


def get_reports(url):
	print "getting links to crimes from: ", url
	doc=parse(url).getroot()
	reports=doc.cssselect('div h2 a')

	for r in reports:	
		crimes[r.attrib['href']]={"status":"new"}

crawl(crime_home)
		
print "---"
print "list of all crime report pages"

for link in links:	
	print home_url+link
	get_reports(home_url+link)
	

for crime in crimes:
	print home+crime	






