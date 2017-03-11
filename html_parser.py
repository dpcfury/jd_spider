# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, new_url, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_data = self._get_new_data(new_url, soup)

        return new_data

    def _get_new_data(self, new_url, soup):
        # 定义每页解析的结果为一个字典{productID,image_url}
        result = {}
        img_node = soup.find("div", id="spec-n1").img
        pid = "JD"+new_url[-15:-5]
        result['productId'] = pid
        # 下柜商品没有图片 src为空串 需要处理
        url = img_node['src'].encode("utf-8")
        if len(url) ==0:
            print "编号为%s的商品已下架" % pid.encode("utf-8")
            return None
        result['imgUrl'] = url

        final_result =[]
        final_result.append(result)
        return final_result
