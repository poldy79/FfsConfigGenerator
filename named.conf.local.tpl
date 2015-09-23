//
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";
acl "intern-s" {
    172.21.0.0/18;
    fd21:b4dc:4b1e::/48;
${ipv4net}
${ipv6net}
};

