# This program allows you to web scrape the CNN "World" Newsfeed.
# Author: Orion F.

import bs4

from bs4 import BeautifulSoup as soup

from urllib.request import urlopen


news_url = "http://rss.cnn.com/rss/cnn_world.rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()
soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")


for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("_"*60)
