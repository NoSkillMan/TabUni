import time
from struct import *
import socket
from scapy.all import *


IFACES.show()
p = sniff(iface="Intel(R) Dual Band Wireless-AC 8265",
          count=10)
print(p)

pingr = IP(dst="192.168.200.254")/ICMP()
# sr1(pingr, iface="Intel(R) Dual Band Wireless-AC 8265")
resp = srloop(pingr, count=5, iface="Intel(R) Dual Band Wireless-AC 8265")


###################


s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)


def icmp():
    global icmp_p
    type = 8
    code = 0
    cs = 0
    id = 0x0001
    seq = 13
    icmp_p = pack("!BBHHH", type, code, cs, id, seq)
    return icmp_p


def ip_header():
    global ip_p
    ip_ihl = 5
    ip_ver = 5
    ip_tos = 0
    ip_tot_len = 0
    ip_id = 54321
    ip_frag_off = 0
    ip_ttl = 8
    ip_proto = socket.IPPROTO_ICMP
    ip_check = 1
    ip_saddr = socket.inet_aton("1.1.1.1")
    ip_daddr = socket.inet_aton("192.168.1.3")
    ip_ihl_ver = (ip_ver << 4) + ip_ihl
    ip_p = pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len, ip_id,
                ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)
    return ip_p


def packet():
    global packet
    packet = ip_p + icmp_p
    print(packet)


icmp()
ip_header()
packet()

while True:
    time.sleep(.1)
    res = s.sendto(packet, ("192.168.31.8", 80))
    print(f'total {res} bytes sent.')
