# !/user/bin/env python
# _*_ coding: utf-8 _*_
from __future__ import print_function, unicode_literals

# -------------module document-----------------------

# _author_='Chen Qian'

# _date_ =''

# _version_ ='1.0'

# ------------module document-------------------------

# ------------module import---------------------------
import os
import csv
import codecs

import requests
from bs4 import BeautifulSoup


# ------------module import---------------------------
class Scraper(object):
    def __init__(self, page):
        self.page = page
        self.url = self.get_url(page)
        self.html = self.get_html(self.url)
        self.fileName = self.createFile()

    def createFile(self):

        'Create file and its name for a certain page'

        # check or create a daily dictionary
        dictionaryName = u'xiamen'
        if not os.path.exists(dictionaryName):
            os.mkdir(dictionaryName)

        fileName = ''.join([dictionaryName, '/', 'ershoufang', '_', str(self.page)])
        return fileName

    def get_url(self, page):
        url_1 = 'http://esf.xm.fang.com/house/i3'
        url_2 = str(self.page)
        url_3 = '/'
        url = ''.join([url_1, url_2, url_3])
        return url

    def get_html(self, url):
        r = requests.get(self.url)
        return r.content

    def parser(self, html):
        soup = BeautifulSoup(self.html)
        container = soup.find('div', attrs={'class': 'houseList'}).find_all('dl')
        for each in container:
            href = 'http://esf.xm.fang.com' + each.find('dt').find('a')['href']

            h = requests.get(href).content
            soup = BeautifulSoup(h)
            info2 = soup.find('div', attrs={'class': 'inforTxt'}).find_all('dl')[0].getText().encode('GB18030')
            print(info2)
            info3 = soup.find('div', attrs={'class': 'inforTxt'}).find_all('dl')[1].getText().encode('GB18030')
            print(info3)
            with codecs.open(self.fileName, 'ab') as f:
                writer = csv.writer(f)
                writer.writerow((info2, info3))


def PageScraper(page):
    'A scraper for a certain page of a certain category'

    # produce the HTML
    scraper = Scraper(page)
    fileName = scraper.fileName
    html = scraper.html
    scraper.parser(html)


def CategoryScraper():
    'A scraper for a certain category'

    for i in range(79, 100):
        # tmallPageScraper(categoryName,catNum,pageNum =i)
        page = i
        PageScraper(i)
        #    t.start()


if __name__ == '__main__':
    # main()
    print('-' * 40)
    CategoryScraper()