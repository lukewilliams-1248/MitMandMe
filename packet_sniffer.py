#!/usr/bin/env python3

import scapy.all as scapy

def packet_sniffer(interface):
    # prn argument allows callback function to let us know a packet was captured and execute a given function
    scapy.sniff(iface=interface, store=False, prn=)

sniff("eth0")