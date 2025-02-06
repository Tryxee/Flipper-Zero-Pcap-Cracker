import os
from scapy.all import rdpcap, wrpcap, EAPOL

def extract_eapol(input_file, output_file):
    try:
        # Read packets from the pcap file
        packets = rdpcap(input_file)

        # Filter packets that contain the EAPOL layer
        eapol_packets = [pkt for pkt in packets if pkt.haslayer(EAPOL)]

        if eapol_packets:
            # Save only EAPOL packets to a new pcap file
            wrpcap(output_file, eapol_packets)
            print(f"✅ Extraction successful: {len(eapol_packets)} EAPOL packets extracted from {input_file}")
        else:
            print(f"⚠️ No EAPOL packets found in {input_file}, skipping file.")

    except Exception as e:
        print(f"❌ Error with {input_file}: {e}")

if __name__ == "__main__":
    input_dir = "../Pcap_files/"
    output_dir = "../EAPOL_Extracted/"

    # Create directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(input_dir, exist_ok=True)

    # Check if input directory contains files
    if not os.listdir(input_dir):
        print(f"⚠️ The directory '{input_dir}' is empty. Add .pcap files before running the script.")
        exit(1)

    print(f"📂 Input directory: {input_dir}")
    print(f"📂 Output directory: {output_dir}\n")

    # Loop through all files in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pcap"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name.replace(".pcap", "_hash.pcap"))

            print(f"🔄 Processing {input_path}...")
            extract_eapol(input_path, output_path)
            print(f"✅ Result saved in {output_path}!\n")
