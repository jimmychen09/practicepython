# http://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
import requests
from bs4 import BeautifulSoup

def NYTimes(url):
	global nyStories
	file = []
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html, "lxml")
	titles = soup.find("body").find_all("title")
	file.append("NY Times Stories\n")
	for i in titles:
		file.append(i.text.replace("Share Article: ", "").replace('"', ""))
		file.append("\n")
	nyStories = "".join(file)
	return nyStories

def SMH(url):
	global smhStories
	file = []
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html, "lxml")
	titles = soup.find("div", {'class':'_1S65r'}).find_all("h3")
	file.append("\nSMH Top Stories\n")
	for i in titles:
		if i.string == "More top stories":
			pass
		else:
			file.append(i.text)
			file.append("\n")
	smhStories = "".join(file)
	return smhStories

NYTimes("https://www.nytimes.com/")
SMH("https://www.smh.com.au/")

with open(input("Select a file name to create: ")+".txt", "w") as open_file:
	open_file.write(nyStories)
	open_file.write(smhStories)