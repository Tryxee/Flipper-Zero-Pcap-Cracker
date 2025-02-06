import os
from scapy.all import rdpcap, wrpcap

def extract_eapol(input_file, output_file):
    try:
        packets = rdpcap(input_file)
        eapol_packets = [pkt for pkt in packets if pkt.hashlayer("EAPOL")]
        wrpcap(output_file, eapol_packets)
    except Exception as e:
        print(f"Erreur avec {input_file}: {e}")

if __name__ == "__main__":
    input_dir = "../Pcap_files"
    output_dir = "../EAPOL_Extracted"
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pcap"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name.replace(".pcap", "_hash.pcap"))
            print(f"Treatement of {input_path}...")
            extract_eapol(input_path, output_path)
            print(f"Result save in {output_path} !")
