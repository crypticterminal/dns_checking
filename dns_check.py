import socket, pdb, json, requests

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

url = "http://150.95.137.240/ask_goo.php"
i = 0
flag = 0
ansli = {}
for web in hotweb:
	ans = socket.gethostbyname(web)
	param = {
		'dn': web,
	}
	r = requests.get(url, params=param)
	data = json.loads(r.text)
	for i in range(len(data['Answer'])):
		if ans == data['Answer'][i]['data']:
			flag = 1
			break
	if flag == 0:
		print(web, " F")
	else:
		print(web, " Safe")

	# ansli[web] = r.json()
	# if data[1] == 'F':
		# print web, " might be DNS Spoofing"
	# ansli[web] = ans
	# print web, "\n", ans, "\n"
# pdb.set_trace()

