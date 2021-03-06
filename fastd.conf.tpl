log to syslog level warn;
interface "vpn${seg}";
method "salsa2012+gmac";    # new method, between gateways for the moment (faster)
method "salsa2012+umac";  
# Bind von v4 and v6 interfaces
bind ${externalipv4}:${port};
bind [${externalipv6}]:${port};

include "secret.conf";
mtu 1406; # 1492 - IPv4/IPv6 Header - fastd Header...
on verify "/root/freifunk/unclaimed.py";
status socket "/var/run/fastd-vpn${seg}.sock";
include peers from "peers";
