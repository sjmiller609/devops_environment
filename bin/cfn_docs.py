#!/usr/bin/env python

# Author: Steven Miller

import requests
import urllib
import sys
import lxml.html as html

want_tags = ['p','h1','h2','h3','div']
want_divs = ['variablelist','aws-note','YAML']

if len(sys.argv) < 2:
    print("usage:\ncfn_docs security group\ncfn_docs ec2")
    exit(0)

# Build URL to query Google
google_url = 'https://www.google.com/search?'
# I'm feeling lucky: go to first result
google_url += 'btnI=1'
# Limit results to only this specific website
google_url += '&as_sitesearch=docs.aws.amazon.com'
# Build query
query = "aws cloudformation "
for arg in sys.argv[1:]:
    query += arg + " "
# This line escapes spaces and the like
query = urllib.quote_plus(query.strip())
# Attach query to URL
url = google_url + "&q=" + query

# Query
response = requests.get(url)

# Parse the raw HTML
parsed = html.fromstring(response.text)

# Print out the HTML elements we want
try:
  main_content = parsed.get_element_by_id("main-col-body")
except KeyError:
  print("Sorry! Did not find a document.")
  print(url)
  exit(0)

content = html.tostring(main_content)
for el in main_content:
  if (el.tag not in want_tags) or \
     (el.tag == 'div') and not ( \
       ('class' in el.attrib.keys() and el.attrib['class'] in want_divs) or \
       ('id' in el.attrib.keys() and el.attrib['id'] in want_divs)
     ):
    continue
  print(html.tostring(el))
