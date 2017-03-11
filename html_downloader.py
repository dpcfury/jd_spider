# -*- coding:utf-8 -*-
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        req = urllib2.Request(url)

        # 请求头的预处理
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")
        req.add_header("Accept","Atext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Host","item.jd.com")

        try:
            response = urllib2.urlopen(req)
            if response.getcode() != 200:
                return None
            return response.read()
        except:
            print "请求出错 请求的地址为 %s" % url.encode("utf-8")
            return None

