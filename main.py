from crawl import Crawl
from extract import Extract
from store import Store

import datetime
from bs4 import BeautifulSoup
import time

class Main(object):
    def __init__(self):
        self.crawl = Crawl()
        self.extract = Extract()
        self.store = Store()

    def __str__(self):
        return '-Building crawl, extract, and store modules-'

    def get_search_info(self, key_word, Initial_time, Deadline):
        """
        Get search information from Weibo based on a keyword and date range.

        Parameters:
        key_word (str): The keyword to search for.
        Initial_time (str): The start date for the search in 'YYYY-MM-DD' format.
        Deadline (str): The end date for the search in 'YYYY-MM-DD' format.

        Returns:
        None
        """
        # Determine the date range
        date_list = self.__set_timelist(Initial_time, Deadline)

        # Loop through each day in the date range
        for i, times in enumerate(date_list, start=1):
            print(f'-Current date progress: [{i}/{len(date_list)}] {times}')
            time.sleep(1)
            for page in range(1, 51):
                print(f'-Current page progress: [{page}/50] {page} page')

                page_info = self.crawl.post_crawl(key_word, times, page)

                soup = BeautifulSoup(page_info, 'lxml')
                no_results = soup.find('div', class_='card-no-result')
                if no_results and "抱歉，未找到相关结果" in no_results.text:
                    print('-No data for the current date or already crawled')
                    break
                else:
                    extract_info = self.extract.post_extract(page_info)
                    print(f'-Extracted information: {extract_info}')

                    self.store.store_post_mode_mysql('WeiboSearch', key_word, extract_info)
                    time.sleep(1)

    def __set_timelist(self, Initial_time, Deadline):
        """
        Create a list of dates between Initial_time and Deadline.

        Parameters:
        Initial_time (str): The start date in 'YYYY-MM-DD' format.
        Deadline (str): The end date in 'YYYY-MM-DD' format.

        Returns:
        list: A list of dates in 'YYYY-MM-DD' format.
        """
        date_list = []
        new_time = datetime.datetime.strptime(Initial_time, "%Y-%m-%d")
        date = Initial_time[:]
        while date <= Deadline:
            date_list.append(date)
            new_time = new_time + datetime.timedelta(1)
            date = new_time.strftime("%Y-%m-%d")
        return date_list
