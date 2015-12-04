#!/usr/bin/env python
# Proof of principle to convert network conf file to iptables entries
import json
import sys
def genEntry(network,description):
	s = "## %s\n" % description
	s = s + "-A INPUT -p tcp --source %s --dport 1024:65535 -j ACCEPT\n" % network
	s = s + "-A INPUT -p udp --source %s --dport 1024:65535 -j ACCEPT" % network
	return s
gen6="-6" in sys.argv
if gen6:
	ttype="ipv6"
else:
	ttype="ipv4"

for f in sys.argv[1:]:
	try:
		fh = open(f,"r")
	except:
		continue
	nets = json.load(fh)
	fh.close()
	for group in nets:
		for sn in group['subnets']:
			desc = sn['name']	
			subnet = sn['subnet']
			type =  subnet['type']
			network = subnet['network']
			if type.lower() == ttype :
				print genEntry(network,desc)

