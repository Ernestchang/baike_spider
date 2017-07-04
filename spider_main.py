import html_downloader, html_outputer, html_parser, url_manager
import urllib.parse

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager() # url管理器
        self.downloader = html_downloader.HtmlDownloader() # HTML下载器
        self.parser = html_parser.HtmlParser() # HTML解析器
        self.outputer = html_outputer.HtmlOutputer() # HTML输出器

    def craw(self, root_url):
        cnt = 1
        self.urls.add_new_url(root_url) # 入口URL加进URL管理器
        while self.urls.has_new_url(): # 当前有可供抓取的URL
            try:
                new_url = self.urls.get_new_url() # 获得新的URL
                print('正在爬取第 %d 个URL：%s' % (cnt, urllib.parse.unquote(new_url))) # 打印次数和URL
                html_cont = self.downloader.download(new_url) # 下载网页内容
                new_urls, new_data = self.parser.parse(html_cont) # 解析网页并获得新的URL和数据
                self.urls.add_new_urls(new_urls) # 新的URL加入管理器
                self.outputer.collect_data(new_data) # 输出器收集数据

                if cnt == 100: #预定爬取1000个网页
                    break

                cnt += 1 # 计数

            except Exception as e: # 异常处理
                print('爬取失败:', e)

        self.outputer.output_html() # HTML输出



if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)