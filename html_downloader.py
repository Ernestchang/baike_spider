import requests

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        response = requests.get(url)
        if response.status_code != 200:
            return None
        response.encoding = 'utf-8'
        return response