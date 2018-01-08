# 11.4 Generating a Range of IP Addresses from a CIDR Address

import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')
# for a in net:
#     print(a)
# 123.45.67.64
# 123.45.67.65
# 123.45.67.66
# ...
# 123.45.67.94
# 123.45.67.95

# Show all available ip address number
#print(net.num_addresses)  # 32

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
# for a in net6:
#     print(a)
# 12:3456:78:90ab:cd:ef01:23:30
# 12:3456:78:90ab:cd:ef01:23:31
# 12:3456:78:90ab:cd:ef01:23:32
# 12:3456:78:90ab:cd:ef01:23:33
# 12:3456:78:90ab:cd:ef01:23:34
# 12:3456:78:90ab:cd:ef01:23:35
# 12:3456:78:90ab:cd:ef01:23:36
# 12:3456:78:90ab:cd:ef01:23:37

# Show all available ipv6 ip address number
#print(net6.num_addresses)  # 8
