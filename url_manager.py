# -*- coding:utf-8 -*-
import xlrd


class UrlManager(object):
    def __init__(self):
        # 选择通过读取excel直接初始化
        self.new_urls = set()
        self.old_urls = set()

        # 预备读excel并将其中的url逐个塞入new_urls集合中进行初始化
        # 打开excel 文件
        data = xlrd.open_workbook('jd.xlsx')
        # 通过名称获取工作表
        table = data.sheet_by_name(u'product')
        # 获取表格的行数和列数
        nrows = table.nrows

        # 从第二行开始讲每行的url读取出来
        print "正在从excel中架子商品的访问路径.........."
        count = 0
        for i in range(1, nrows):
            row_values = table.row_values(i)
            url = row_values[4]
            # 添加进url集合中
            self.add_new_url(url)
            count += 1
        print "从excel加载url完成 共加载%d项" % count

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def print_urls(self):
        print "url的总个数为:%d" % len(self.new_urls)
        for url in self.new_urls:
            print "url:" + url
