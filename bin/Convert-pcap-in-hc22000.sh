#!/bin/bash

# Check if hcxtools is installed
if ! command -v hcxpcaptool &> /dev/null; then
    echo "❌ hcxtools is not installed. Please install it first."
    exit 1
fi

# Input and output directories
pcap_dir="../EAPOL_Extracted"
hash_dir="../hashs"
mkdir -p "$hash_dir"

# Vérifier s'il y a au moins un fichier .pcap
shopt -s nullglob  # Empêche l'erreur si aucun fichier ne correspond
pcap_files=("$pcap_dir"/*.pcap)

if [[ ${#pcap_files[@]} -eq 0 ]]; then
    echo "❌ No .pcap files found in $pcap_dir."
    exit 1
fi

# Traitement des fichiers .pcap
echo "🔄 Processing .pcap files in $pcap_dir..."
hcxfile="$hash_dir/hashed.hc22000"  # Nom de fichier fixe

for file in "${pcap_files[@]}"; do
    if [[ -f "$file" && -r "$file" ]]; then
        echo "⚙️  Converting: $(basename "$file")"
        hcxpcaptool -o "$hcxfile" "$file"
    else
        echo "⚠️  Skipping unreadable file: $file"
    fi
done

echo "✅ Conversion complete. Output saved in: $hcxfile"
