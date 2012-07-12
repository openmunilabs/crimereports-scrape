import feedparser
import urllib

from lxml.html import parse,document_fromstring
import lxml

import re

crimepages="data/crimepages.txt"

f=open(crimepages)

crimes=[]
stolen=[]


date_expr = r"\d{1,2}/\d{2}/\d{2}"

for line in f:
	line=line.strip()
	name=line.split("/")[5].split(".")[0]
	name=name.split("-")
	name=name[2]+"-"+name[3]+"-"+name[4]
	print name
	
	fi=open("data/raw/"+name+".html")
	
	body=fi.read().strip()
	
	doc=document_fromstring(body)
	filtered=doc.cssselect('div.wrapContent div')
	
	
	is_crime=True
	is_auto=False
	
	for r in filtered:	
		content=r.text_content().strip("\n")
		
		#print "~~~"
		#print content
		if re.search(date_expr, content) is None:
			#print "true:", content
			pass
		elif re.search("block of", content) is None:
			#print "true:", content
			pass
		else: 
			print content
			print "---"



