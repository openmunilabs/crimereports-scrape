
import feedparser
import urllib

from lxml.html import parse


#proto code to extract crimes list from single crime page for particular date


url="http://news.arlingtonva.us/crime-report:-may-16-2013"
#url="http://news.arlingtonva.us/crime-reports-april-27-2011-202323"

crimes=[]
stolen=[]

def get_crimes(url):

	doc=parse(url).getroot()
	reports=doc.cssselect('div.wrapContent p span span')
	
	for r in reports:	
		content=r.text_content().strip()
		print content

	return

"""
	is_crime=True
	is_auto=False
	
	buff=""
	for r in reports:	
		content=r.text_content().strip()
		print content
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
			
"""
get_crimes(url)

print crimes

print stolen