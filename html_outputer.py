# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect(self, new_data):
        if new_data is None:
            return
        self.data = self.data + new_data # 发现一个问题如果直接是list.append来添加字典结果 会出现第二个结果开始出现的None

    def output_txt(self):
        # 追加写入文件
        f = open('img_urls.txt', 'a')
        for item in self.data:
            print "ID:%s ,image_url:%s" % (item.get("productId"), item.get("imgUrl"))
            f.write("%s :: %s\n" % (item.get("productId"), item.get("imgUrl")))
        f.close()

        self.data = []
