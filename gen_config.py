#!/usr/bin/python
from string import Template
from netaddr import *
import argparse


def genNetwork(segments, gw):
	fp = open("ffs-gw.tpl","rb")
	tmpl = Template(fp.read())
	fp.close()
	ip = IPNetwork("10.190.0.0/18")

	for seg in segments:
		ipv4 = str(ip.network+gw)
		inst = tmpl.substitute(gw="0%i"%(gw),seg=seg,ipv4=ipv4)
		fp = open("etc/network/interfaces.d/ffs-gw%s%i"%(seg,gw), "wb")
		fp.write(inst)
		fp.close()
		ip = IPNetwork(str(ip.broadcast+1)+"/18")


def genRadvd(segments, gw):
	fp = open("radvd.conf.tpl")
	tpl = Template(fp.read())
	fp.close()
	fp = open("etc/radvd.conf","wb")
	for seg in segments:
		inst = tpl.substitute(gw="0%i"%(gw),seg=seg)
		fp.write(inst)
	fp.close()

def genDhcp(segments, gw):
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
		ipv4gw = str(ip.network+gw)
		dhcp_ipnet = IPNetwork("%s/21"%(ip.network))
		for  i in range(1,gw):
			dhcp_ipnet = dhcp_ipnet.next()
		
		ipv4start = str(dhcp_ipnet.network+10)
		ipv4end = str(dhcp_ipnet.broadcast-1)
		
		inst = tpl.substitute(ipv4start=ipv4start,ipv4end=ipv4end,ipv4net=ipv4net,ipv4gw=ipv4gw)
		fp.write(inst)
		ip = ip.next()
	fp.close()


segments = ["01","02","03","04"]
gw=2
genNetwork(segments,gw)
genRadvd(segments,gw)
genDhcp(segments,gw)
