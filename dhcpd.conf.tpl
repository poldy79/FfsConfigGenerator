subnet ${ipv4net} netmask 255.255.192.0 {
    authoritative;
    pool
    {
     range ${ipv4start} ${ipv4end};
     allow all clients;
    }
    option routers ${ipv4gw};
    option domain-name-servers ${ipv4gw};
}
