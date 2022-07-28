from tkinter import N
from traceback import print_tb
from unicodedata import name
from bs4 import BeautifulSoup


import requests

response = requests.get("https://news.ycombinator.com/newest")
yc_Web_page = response.text

soup = BeautifulSoup(yc_Web_page, "html.parser")

article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.select_one(selector="a div", class_="votearrow")
print(article_upvote)
































# with open("./Webscrap/website.html", encoding="utf8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# all_anchors = soup.find_all(name="a")
# # print(all_anchors)

# # for tags in all_anchors:
    
# #     # print(tags.getText())
# #     print(tags.get("href"))
    

# heading = soup.find(name="h1", id="name")
# # print(heading.text)


# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)

# company_heading = soup.select_one(selector="p a")
# # print(company_heading)

# all_heading = soup.select(".heading")
# print(all_heading)