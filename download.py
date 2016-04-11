#!/usr/bin/env python
import urllib2
import json

maxitem_url = 'https://hacker-news.firebaseio.com/v0/maxitem.json'
item_url = 'https://hacker-news.firebaseio.com/v0/item/%s.json'

def get_max_item():
        result = hn_req(maxitem_url)
        return result[0]

def get_item(id):
        url = (item_url % id)
        print "getting " + url
        result = hn_req(url)
        #return json.loads(result[0])
        return result[0]

def hn_req(url):
        req  = urllib2.Request(url)
        result = urllib2.urlopen(req)
        return result.readlines()

def save_item(id):
        filename = './items/%s.txt' % id
        content = get_item(id)
        f = open(filename, 'w')
        f.write(content)
        f.close()

max_item = get_max_item()
for id in range(1, max_item):
	save_item(id)
