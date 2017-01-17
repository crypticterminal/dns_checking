import socket, json, requests

hotweb = ['http://www.plurk.com', 
	'http://www.linkedin.com', 
	'http://www.instagram.com', 
	'http://www.twitch.tv', 
	'http://www.trello.com', 
	'http://www.flickr.com', 
	'http://www.doodle.com', 
	'http://www.pchome.com.tw', 
	'http://www.starbucks.com.tw', 
	'http://www.mobile01.com', 
	'http://www.momoshop.com.tw', 
	'http://shopping.pchome.com.tw', 
	'http://www.books.com.tw', 
	'http://ppt.cc', 
	'http://www.dgpa.gov.tw', 
	'http://www.cwb.gov.tw',
	]

url = "https://dns.google.com/resolve"
i = 0
flag = 0
ansli = {}
for web in hotweb:
	ans = socket.gethostbyname(web)
	param = {
		'name': web,
	}
	r = requests.get(url, params=param)
	data = r.json()
	for i in range(len(data['Answer'])):
		if ans == data['Answer'][i]['data']:
			flag = 1
			break
	if flag == 0:
		print(web, " F")
	else:
		print(web, " Safe")
