import socket, pdb, json, requests

hotweb = [
	'facebook.com', 
	'plurk.com', 
	'google.com', 
	'linkedin.com', 
	'instagram.com', 
	'twitter.com', 
	'twitch.tv', 
	'github.com', 
	'dropbox.com', 
	'trello.com', 
	'flickr.com', 
	'slack.com', 
	'doodle.com', 
	'wikipedia.org', 
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
		print web, " F"
	else:
		print web, " Safe"

	# ansli[web] = r.json()
	# if data[1] == 'F':
		# print web, " might be DNS Spoofing"
	# ansli[web] = ans
	# print web, "\n", ans, "\n"
# pdb.set_trace()

