# -*- coding:utf-8 -*-
import urllib2

from bs4 import BeautifulSoup

test_url = "http://item.jd.com/1000061150.html"
response = urllib2.urlopen(test_url)

if response.getcode() == 200:
    http_cont = response.read()
    soup = BeautifulSoup(http_cont, "html.parser", from_encoding="utf-8")
    print soup.prettify()
    next_node = soup.find("div", id="spec-n1").img
    if next_node is not None:
        print "图片的连接地址为:%s " % next_node['src'].encode("utf-8")
else:
    print "请求为空"