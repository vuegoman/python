from bs4 import *
import requests as rq
import os

r2 = rq.get("https://www.pexels.com/@hiteshchoudhary")
soup2 = BeautifulSoup(r2.text, "html.parser")

links = []

x = soup2.select('img[src^="https://images.pexels.com/photos"]')

for img in x:
  links.append(img['src'])

for l in links:
  print(l)