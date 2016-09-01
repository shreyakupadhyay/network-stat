import re
import subprocess

"""
getting mac address
"""
def getMac():
	proc = subprocess.Popen('ifconfig', stdout=subprocess.PIPE)
	regex = "(.+?)\s*"+re.escape("Link encap:Ethernet  HWaddr ")+"(.+?)\s"
	mac = re.findall(re.compile(regex),proc.stdout.read())
	if not mac:
		print "NO INTERFACE IS FOUND"
	else:
		print mac
getMac()
