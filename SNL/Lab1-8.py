import pcap
import libpcap
import ctypes
from winpcapy import WinPcapUtils
import binascii

arp_request_hex_template = "%(dst_mac)s%(src_mac)s08060001080006040001" \
                           "%(sender_mac)s%(sender_ip)s%(target_mac)s%(target_ip)s" + "00" * 18
packet = arp_request_hex_template % {
    "dst_mac": "aa"*6,
    "src_mac": "bb"*6,
    "sender_mac": "bb"*6,
    "target_mac": "cc"*6,
    # 192.168.0.1
    "sender_ip": "c0a80001",
    # 192.168.0.2
    "target_ip": "c0a80002"
}
# Send the packet (ethernet frame with an arp request) on the interface
WinPcapUtils.send_packet("*Ethernet*", binascii.hexlify(packet.encode()))


sniffer = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)


def addr(pkt, offset):
    return '.'.join((str(pkt[i]) for i in range(offset, offset + 4)))

# bp-f filter for get http packets on port 80
# sniffer.setfilter(
#     "tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)")


for ts, pkt in sniffer:
    print(f'{int(ts)} SRC: {addr(pkt, sniffer.dloff + 12)} DST: {addr(pkt, sniffer.dloff + 16)}')
    # print(pkt[24:].decode('ascii', 'ignore')) #if u want data of packet
