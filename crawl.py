import requests

class Crawl(object):

    def post_crawl(self, keyword, time, page):
        """
        Crawl posts from Weibo based on a keyword and time range.

        Parameters:
        keyword (str): The keyword to search for.
        time (str): The date for the time range in the format 'YYYY-MM-DD'.
        page (int): The page number to crawl.

        Returns:
        str: The HTML content of the response.
        """
        cookies, headers = self.__post_setting()
        url = f'https://s.weibo.com/weibo?q={keyword}&typeall=1&suball=1&timescope=custom%3A{time}-0%3A{time}-23&Refer=g&page={page}'
        resp = requests.get(url=url, headers=headers, cookies=cookies)
        return resp.text

    def __post_setting(self):
        """
        Set the cookies and headers for Weibo requests.

        Returns:
        tuple: Cookies and headers for the request.
        """
        self.cookies = {
            'SINAGLOBAL': '9501109656994.648.1715309424073',
            'UOR': ',,cn.bing.com',
            'SUB': '_2A25LZfm4DeRhGeFG6FQZ8CvMzDSIHXVoG3NwrDV8PUNbmtAGLVDGkW9Nebxey2NdTtXiYNGN84ovx42ociESFJte',
            'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWNwX7z0VwFSicgpSNL.Oeo5JpX5KzhUgL.FoMRe0qReh-7S0n2dJLoI7_iqcHL9Kz7ehn7SBtt',
            'ALF': '02_1720260329',
            'PC_TOKEN': 'fc4831871d',
            '_s_tentry': 'weibo.com',
            'Apache': '2286212657060.6465.1717668765870',
            'ULV': '1717668765943:3:1:1:2286212657060.6465.1717668765870:1716037998864',
        }
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://weibo.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }
        return self.cookies, self.headers
