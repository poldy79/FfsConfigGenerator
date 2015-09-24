log to syslog level warn;
interface "vpn${seg}";
method "salsa2012+gmac";    # new method, between gateways for the moment (faster)
method "salsa2012+umac";  
# Bind von v4 and v6 interfaces
bind 46.101.136.200:${port};
bind [2a03:b0c0:3:d0::13f:f001]:${port};

include "secret.conf";
mtu 1406; # 1492 - IPv4/IPv6 Header - fastd Header...
on verify "/root/freifunk/unclaimed.py";
status socket "/var/run/fastd-vpn${seg}.sock";
include peers from "peers";
