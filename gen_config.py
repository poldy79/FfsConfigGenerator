#!/usr/bin/python
from string import Template
from netaddr import *

segments = ["01","02","03","04"]
gw=1

fp = open("ffs-gw.tpl","rb")
tmpl = Template(fp.read())
fp.close()
ip = IPNetwork("10.190.0.0/18")

for seg in segments:
	inst = tmpl.substitute(gw="0%i"%(gw),seg=seg,ipv4=str(ip.network+1))
	fp = open("etc/network/interfaces.d/ffs-gw%s%i"%(seg,gw), "wb")
	fp.write(inst)
	fp.close()
	ip = IPNetwork(str(ip.broadcast+1)+"/18")



fp = open("radvd.conf.tpl")
tpl = Template(fp.read())
fp.close()
fp = open("etc/radvd.conf","wb")
for seg in segments:
	inst = tpl.substitute(gw="0%i"%(gw),seg=seg)
	fp.write(inst)
fp.close()


fp = open("dhcpd.conf.tpl")
tpl = Template(fp.read())
fp.close()
fp = open("dhcpd.conf.head")
head = fp.read()
fp.close()


fp = open("etc/dhcp/dhcpd.conf","wb")
fp.write(head)
ip = IPNetwork("10.190.0.0/18")

for seg in segments:
	ipv4net = str(ip.network)
	ipv4gw = str(ip.network+1)
	ipv4start = str(ip.network+2)
	ipv4end = str(ip.broadcast-1)
	inst = tpl.substitute(ipv4start=ipv4start,ipv4end=ipv4end,ipv4net=ipv4net,ipv4gw=ipv4gw)
	fp.write(inst)
	ip = IPNetwork(str(ip.broadcast+1)+"/18")
fp.close()

