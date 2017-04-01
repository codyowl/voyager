import urllib2
from bs4 import BeautifulSoup

url = "https://geoiptool.com/"

requester = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
connector = urllib2.urlopen(requester)
connector_reader = connector.read()
soup = BeautifulSoup(connector_reader, "lxml")


country = soup.findAll("div", {"class" : "data-item"})

details_list = []





