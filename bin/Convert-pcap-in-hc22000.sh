# Check if the hcxtools is installed
if ! command -v hcxpcaptool &> /dev/null; then
    echo "hcxtools is not installed. Please install it first."
    exit 1
fi

# Répertoire contenant les fichiers pcap
pcap_dir="../EAPOL_Extracted"

# Dossier de sortie pour les fichiers hash
hash_dir="../hashs"
mkdir -p "$hash_dir"

# Parcourir tous les fichiers .pcap du dossier
for file in "$pcap_dir"/*.pcap; do
    if [[ -f "$file" && -r "$file" ]]; then
        # Définir le nom du fichier de sortie comme "hashed.hc22000"
        hcxfile="$hash_dir/hashed.hc22000"
        
        # Convertir pcap en hc2200
        hcxpcaptool -o "$hcxfile" "$file"
    fi
done

echo "Conversion and organization complete."
