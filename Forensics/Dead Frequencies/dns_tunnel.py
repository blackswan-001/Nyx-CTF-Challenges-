from scapy.all import *

# Flag split into 4 chunks, Base64 encoded
# NYX{d3ad_ | fr3qu3 | nc13s_ | n3v3r_l13}

import base64

chunks = [
    ("01", "NYX{d3ad_"),
    ("02", "fr3qu3"),
    ("03", "nc13s_"),
    ("04", "n3v3r_l13}"),
]

packets = []
src_ip = "192.168.1.100"
dns_ip = "10.0.0.1"

for seq, chunk in chunks:
    encoded = base64.b64encode(chunk.encode()).decode()
    subdomain = f"seq{seq}.{encoded}.corp-sync.internal"

    # DNS Query
    query = (
        IP(src=src_ip, dst=dns_ip)/
        UDP(sport=54321, dport=53)/
        DNS(
            id=int(seq),
            rd=1,
            qd=DNSQR(qname=subdomain, qtype="TXT")
        )
    )

    # DNS Response with TXT record
    response = (
        IP(src=dns_ip, dst=src_ip)/
        UDP(sport=53, dport=54321)/
        DNS(
            id=int(seq),
            qr=1,
            aa=1,
            rd=1,
            ra=1,
            qd=DNSQR(qname=subdomain, qtype="TXT"),
            an=DNSRR(
                rrname=subdomain,
                type="TXT",
                ttl=60,
                rdata=encoded
            )
        )
    )

    packets.append(query)
    packets.append(response)

wrpcap("dns_layer.pcap", packets)
print(f"[+] dns_layer.pcap written — {len(packets)} packets")