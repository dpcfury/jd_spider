jd_spider

- spider_main是爬虫的主入口
- url_manger 负责进行url的保存和管理
- html_downloader 负责进行请求的发送和解析
- html_parser负责解析爬取到的页面
- html_ouputer负责暂存爬取到的数据和输出



主要涉及到的python工具包:

- urllib2
- BeautifulSoup4
- xlrd 
- xlwt



jd.xlsx是一份13年京东商品数据，存有对应商品的访问地址，我们做的是从地址中找出一张对应的商品图片的url。