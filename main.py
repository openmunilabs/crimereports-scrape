import requests
from lxml.html import parse
import json
import os
import base64
import codecs
import StringIO


# Crime reports home page for Arlington, VA 
arlingtonva_home="http://news.arlingtonva.us"
crimes_home="http://news.arlingtonva.us/police/crimereports"

#See page above an put total num of pages here
num_pages=44

#Links to every daily crime report page
links=[]

#To avoid overscraping, save list of collected links in json file first time, and use it later
daily_pages_file="data/daily_pages_urls.json"
if os.path.isfile(daily_pages_file):
	f=open(daily_pages_file)
	links=json.loads(f.read())
	f.close()
else:
	#Scan every single page for links to actual daily crime reports
	for i in range(1,num_pages+1):
		url = crimes_home+"?page="+str(i)
		#print url

		page = parse(url).getroot()

		reports=page.cssselect('div.newsBody.clearfix h2 a')

		for report in reports:
			daily_url=arlingtonva_home+report.attrib['href']
			#print daily_url
			links.append(daily_url)

	f=open(daily_pages_file, "w")
	f.write(json.dumps(links, indent=4))
	f.close()

#print links 

#now let's download individual pages and dump them into data/raw/ folder
for link in links:
	file_name = "data/raw/"+base64.urlsafe_b64encode(link)+".html"
	if not os.path.isfile(file_name):
		#print "downloading: ",link
		f=codecs.open(file_name, "w", "utf-8")

		request=requests.get(link)
		body=request.text
		f.write(body)
		f.close()
	else:
		#print "already exists: ",link
		pass


chunks=[]

#Time to extract daily crime messages from downloaded data
for link in links:
	file_name = "data/raw/"+base64.urlsafe_b64encode(link)+".html"
	if os.path.isfile(file_name):
		f=codecs.open(file_name, "r", "utf-8")
		data=f.read()
		f.close()

		#parser = etree.HTMLParser()
		doc   = parse(StringIO.StringIO(data)).getroot()

		reports=doc.cssselect('div.wrapContent p span span')
		
		for r in reports:	
			content=r.text_content().strip()
			print "---"
			print content
			chunks.append(content)
	else:
		print "file %s is missing??" % (file_name)




