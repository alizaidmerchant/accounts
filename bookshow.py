import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.igp.com/friendship-day-gifts/personalized-gifts/jewellery?adgroupid=1274334784933549&device=c&keyword=personalized%20gifts%20&loc_interest_ms=148579&loc_physical_ms=1656&feeditemid=&adposition=&msclkid=95c6c7d1c38a1d680af8a2ffaaa58101&utm_source=bing&utm_medium=cpc&utm_campaign=DSA-Feedbased_India_21&utm_term=personalized%20gifts%20&utm_content=Feed%20based"

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")
names = soup.find_all("p",{"class":"product-name product-name-revamp Paragraph-14-S--Semibold"})
# print(len(names))

for name in names:
    print(name.text)

# prices = soup.find_all("p",{"class":"product-price product-price-revamp"})
# print(len(prices))

# for price in prices:
    # print(len(price))

reviews = soup.find_all("span",{"class":"prd-rtn-str Paragraph-12-XS--Regular"})
# print(len(reviews))

for review in reviews:
    print(review.text)

df = pd.DataFrame({"Product_name":names,"Reviews":reviews})
print(df)

df.to_csv("D:\ALIZAID ITR/data.csv")