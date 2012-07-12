import feedparser
import urllib

from lxml.html import parse

url="http://news.arlingtonva.us/pr/ava/crime-reports.aspx?q=&s=relevance&ncid=29841&pg=6#ltIndexCurrentPage2"

crimes={}

def get_reports(url):

	doc=parse(url).getroot()
	reports=doc.cssselect('div h2 a')

	for r in reports:	
		crimes[r.attrib['href']]={"status":"new"}


get_reports(url)

print crimes

