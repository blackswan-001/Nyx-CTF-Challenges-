from scapy.all import *
import random, string

def random_domain():
    tld = random.choice(["com", "net", "org", "io"])
    name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))
    return f"{name}.{tld}"

packets = []

# ICMP noise — 40 pings to random IPs
for i in range(40):
    ip = f"192.168.{random.randint(1,254)}.{random.randint(1,254)}"
    packets.append(
        IP(dst=ip)/ICMP()/Raw(load=b"A"*random.randint(20,60))
    )

# DNS noise — 30 queries to random domains, all A record, no answers
for i in range(30):
    domain = random_domain()
    packets.append(
        IP(src="192.168.1.100", dst="8.8.8.8")/
        UDP(sport=random.randint(1024,65535), dport=53)/
        DNS(rd=1, qd=DNSQR(qname=domain, qtype="A"))
    )

# Fake ARP noise — 20 packets
for i in range(20):
    ip = f"192.168.1.{random.randint(2,254)}"
    packets.append(
        Ether(dst="ff:ff:ff:ff:ff:ff")/
        ARP(pdst=ip)
    )

wrpcap("noise_layer.pcap", packets)
print(f"[+] noise_layer.pcap written — {len(packets)} packets")