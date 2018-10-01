#http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")

titles = soup.find("body").find_all("title")

print("NY Times Stories")
for i in titles:
	print(i.text.replace("Share Article: ", "").replace('"', ""))


url = "https://www.smh.com.au/"

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")

titles = soup.find("div", {'class':'_1S65r'}).find_all("h3")

print("\nSMH Top Stories")
for i in titles:
	if i.string == "More top stories":
		pass
	else:
		print(i.text)