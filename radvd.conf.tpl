interface br${seg}
{
    AdvSendAdvert on;
    IgnoreIfMissing on;
    MaxRtrAdvInterval 200;

    # don't advertise default router
    AdvDefaultLifetime 0;

    prefix fd21:b4dc:4b${seg}::/64
    {};

    RDNSS fd21:b4dc:4b${seg}::a38:${gw}
    {};

    route fd21:b4dc:4b00::a38:1/128
    {
    };
	 
};
