# coding=UTF-8
import socket, pdb, json, requests, pcap, dpkt

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

trash = [ '172.217.27.142', '31.13.95.8', '172.217.27.131', '210.242.43.152', '210.242.216.152', '157.7.180.133', '192.30.253.125', '91.108.56.154', '117.18.232.133', '216.58.200.232', '64.233.187.188' ]

me = '192.168.1.6'
url = "http://150.95.137.240/find.php"

def RAPac(target):
	iplist = []
	f = open('trytcp_hack.pcapng')
	pcap = dpkt.pcap.Reader(f)
	for ts, buf in pcap:
		eth = dpkt.ethernet.Ethernet(buf)
		ipall = eth.data
		if eth.type == dpkt.ethernet.ETH_TYPE_IP and ipall.p == 6:
			ipd = '%d.%d.%d.%d' % tuple(map(ord,list(ipall.dst)))
			ips = '%d.%d.%d.%d' % tuple(map(ord,list(ipall.src)))
			if ips != me and ips not in iplist and ips not in trash:
				iplist.append(ips)
			elif ipd != me and ipd not in iplist and ipd not in trash:
				iplist.append(ipd)

	return iplist

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
	else:
		print(web, " Safe")
	# ansli[web] = ans
	# print web, "\n", ans, "\n"
# pdb.set_trace()



