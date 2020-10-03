import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

#Opeing up connection, grabbing the page
my_url = 'https://www.aljazeera.com/'
uClient = uReq(my_url) 
page_html = uClient.read()
uClient.close()

#html_parsing
page_soup = Soup(page_html, "html.parser")

#grabs each item
containers = page_soup.findAll("a", {"class" : "fte-featured__excerpt__link fte-featured__title__link"})
linkContainer = page_soup.findAll("div", {"class" : "fte-featured__right-small-article-image"})

filename = "news.csv"
filename1 = "newsLink.csv"

f = io.open(filename, "w", encoding="utf-8")
f1 = io.open(filename1, "w", encoding="utf-8")

headers = "new_title\n"
headers1 = "news_links\n"

f1.write(headers1)
for container in linkContainer:
    news_links = container.a.get('href')
    f1.write("https://www.aljazeera.com" + news_links + "\n")
f1.close()

f.write(headers)
for container in containers:
    news_title = container.text
    f.write(news_title.replace(","," ") + "\n")
f.close()

##########################################################################################################

#Opeing up connection, grabbing the page
my_url1 = 'https://www.bbc.com/news/'
uClient1 = uReq(my_url1) 
page_html1 = uClient1.read()
uClient1.close()

#html_parsing
page_soup1 = Soup(page_html1, "html.parser")

#grabs each item
containers1 = page_soup1.findAll("a", {"class" : "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})

#linkContainer1 = page_soup1.findAll("a", {"href" : "fte-featured__right-small-article-image"})

filename2 = "bbcNews.csv"
filename3 = "bbcNewsLink.csv"

f = io.open(filename2, "w", encoding="utf-8")
f1 = io.open(filename3, "w", encoding="utf-8")

headers = "new_title\n"
headers1 = "news_links\n"

f1.write(headers1)
for container in containers1:
    news_links = container.get('href')
    f1.write("https://www.bbc.com" + news_links + "\n")
f1.close()

f.write(headers)
for container in containers1:
    news_title = container.text
    f.write(news_title.replace(","," ") + "\n")
f.close()