import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["3/minute"])

@app.route("/facebook/profile-id", methods=['GET'])
def facebook_profile_id():
	url = request.args.get('url')
	if url != "":
		ids = scrape_facebook_profile_id(url)
		if ids.__len__() != 0:
			return jsonify(ids)
		else:
			return jsonify([])
	else:
		return "url param not found", 400

def scrape_facebook_profile_id(reference_url):
	page = requests.get(reference_url.strip())
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
		return profile_id
	else:
		return []
