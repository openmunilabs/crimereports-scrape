
import feedparser
import urllib

from lxml.html import parse

url="http://news.arlingtonva.us/pr/ava/crime-report-may-21-2012-234244.aspx?ncid=29841"
#url="http://news.arlingtonva.us/pr/ava/crime-reports-june-6-2011-207727.aspx?ncid=29841"

crimes=[]
stolen=[]

def get_crimes(url):

	doc=parse(url).getroot()
	reports=doc.cssselect('div.wrapContent div')

	reports=doc.cssselect('div.wrapContent')
	
	print reports[0].text_content()
	
	return

	is_crime=True
	is_auto=False
	
	buff=""
	for r in reports:	
		content=r.text_content().strip()
		if content=="REPORTS":
			is_crime=True
			is_auto=False
		if content=="STOLEN VEHICLES":
			is_crime=False
			is_auto=True

		if is_crime and len(content)>20 and content!="REPORTS":
			crimes.append(content)
			print "crime: ", content
		if is_auto and len(content)>20  and content!="STOLEN VEHICLES":
			if buff=="":
				buff=buff+content
			else:
				stolen.append(buff+"; "+content)
				buff==""
				print "auto: ", buff,"; ",content
			

get_crimes(url)

print crimes

print stolen