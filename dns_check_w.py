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

url = "http://150.95.137.240/find.php"

ansli = {}
for web in hotweb:
	ans = socket.gethostbyname(web)
	param = {
		'dn': web,
		'ip': ans,
	}
	r = requests.get(url, params=param)
	data = r.json()
	ansli[web] = r.json()
	if data[1] == 'F':
		print(web, " might be DNS Spoofing")
	# ansli[web] = ans
	# print web, "\n", ans, "\n"
# pdb.set_trace()

