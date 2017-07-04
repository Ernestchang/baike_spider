from bs4 import BeautifulSoup
import re, urllib.parse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /item/Python
        links = soup.find_all('a', href = re.compile(r'/item/')) # 获取网页内所有新URL
        for link in links: # 逐条处理
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url) # 补充完整
            new_urls.add(new_full_url) # 加入URL集合
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = 'lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, html_cont):
        if html_cont is None:
            return

        page_url = html_cont.url
        soup = BeautifulSoup(html_cont.text, 'lxml')

        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data