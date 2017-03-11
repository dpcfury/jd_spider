# -*- coding:utf-8 -*-
import time
import html_downloader
import html_outputer
import url_manager
import html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):
        count = 1
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print "正抓取第%d个页面 : %s....." % (count, new_url.encode("utf-8"))
            html_cont = self.downloader.download(new_url)
            # 其中有302暂时性重定向需要略过处理
            if html_cont is None:
                continue

            # 解析出其中的图片路径
            new_data = self.parser.parser(new_url, html_cont)
            # 设置了在某些特殊情况下返回的为空
            if new_url is None:
                continue

            # 存入结果的暂存集准备输出
            self.outputer.collect(new_data)
            count += 1

            # 抓取2个页面休眠一次
            if count % 2 == 0:
                time.sleep(2)

            # 读100个写一次防止失败
            if count % 10 == 0:
                # 写如文件一次
                self.outputer.output_txt()
                time.sleep(10)

if __name__ == "__main__":
    spider = SpiderMain()
    spider.craw()
