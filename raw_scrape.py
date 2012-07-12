import feedparser
import urllib

from lxml.html import parse
import lxml

crimepages="data/crimepages.txt"

f=open(crimepages)

for line in f:
	line=line.strip()
	name=line.split("/")[5].split(".")[0]
	name=name.split("-")
	name=name[2]+"-"+name[3]+"-"+name[4]
	print name
	
	url=line
	doc=parse(url).getroot()
	
	fo=open("data/raw/"+name+".html","w")
	fo.write(lxml.html.tostring(doc.body))
	fo.close()
	
	
"""

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

"""




