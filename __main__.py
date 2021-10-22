import requests
from bs4 import BeautifulSoup

URL = "https://www.facebook.com/matheus064/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
meta_elements = soup.find_all("meta")

profile_tags = []
profile_id = []

for m in meta_elements:
	if "profile" in m.__str__():
		profile_tags.append(m.__str__())

if profile_tags.__len__() != 0:
	for p_tag in profile_tags:
		splitted = p_tag.split(" ")
		splitted = "".join(splitted)
		splitted = splitted.split("/profile/")
		splitted = splitted[1]
		splitted = splitted.split("\"")[0].strip()
		profile_id.append(splitted)

if profile_id.__len__() != 0:
	print(profile_id)