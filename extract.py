from bs4 import BeautifulSoup

class Extract(object):
    def post_extract(self, page_info):
        """
        Extract post information from the HTML content of a Weibo search results page.

        Parameters:
        page_info (str): HTML content of the Weibo search results page.

        Returns:
        list: A list of dictionaries containing extracted post information.
        """
        post_list = []

        new_page_info = BeautifulSoup(page_info, 'lxml')
        data_list = new_page_info.find_all('div', class_="card")

        for i in data_list:
            try:
                dic = {}
                # Publisher ID
                dic['publisher_id'] = i.find('div', class_="info").find('a', target="_blank").text

                # Publication time and link
                time_info = i.find('div', class_="from").find('a')
                dic['publication_time'] = time_info.text.strip().replace('\n', '').replace(' ', '').replace('来自', '')
                dic['link'] = time_info['href']

                # Forward count
                dic['forward_count'] = str(i.find_all('a', class_="woo-box-flex woo-box-alignCenter woo-box-justifyCenter")[-3].text).replace(' ', '')
                if dic['forward_count'] == '转发':
                    dic['forward_count'] = '0'

                # Thumbs up count (likes)
                dic['like_count'] = str(i.find_all('span', class_="woo-like-count")[-1].text).replace(' ', '')
                if dic['like_count'] == '赞':
                    dic['like_count'] = '0'

                # Comment count
                dic['comment_count'] = str(i.find_all('a', class_="woo-box-flex woo-box-alignCenter woo-box-justifyCenter")[-2].text).replace(' ', '')
                if dic['comment_count'] == '帖子转发':
                    dic['comment_count'] = '0'

                # Content
                dic['content'] = str(i.find('p', class_="txt").text).replace('\n', '').replace(' ', '').replace('\u200b', '').replace('收起', '')

                post_list.append(dic)
            except:
                pass

        return post_list
