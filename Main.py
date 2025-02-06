"""
./bin :
./bin/Convert-pcap-in-hc2200.sh
./bin/extract-eapol.py

./hashs :
Hash files Folder

./Pcap_files:
Pcap files Folder

./wordlists :
./wordlists/Generate_Wordlist.py
default wordlists : 10million.txt, rockyou.txt
"""

import os
import subprocess
from time import sleep as wait

def extract_eapol():
    """ Exécute le script pour extraire les EAPOL """
    try:
        subprocess.run("python ./bin/extract-eapol.py", shell=True, check=True)
        print("Extracting EAPOL...")
        wait(0.5)
        print("EAPOL Extracted")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during EAPOL extraction: {e}")
        return False

def convert_in_hc22000():
    """ Exécute le script pour convertir les fichiers en hc22000 """
    try:
        subprocess.run("chmod +x ./bin/Convert-pcap-in-hc2200.sh && bash ./bin/Convert-pcap-in-hc2200.sh", shell=True, check=True)
        wait(0.5)
        print("Conversion done!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return False

def hashcat(wordlists, w_choosed):
    """ Lance Hashcat avec la wordlist choisie """
    file = "./hash/hashed.hc22000"
    try:
        subprocess.run(f"hashcat -m 22000 {file} {wordlists[w_choosed]}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Hashcat: {e}")

if __name__ == "__main__":
    try:
        subprocess.run("clear", shell=True)

        print("\nWelcome to Crack-Pcap!\n\n")
        wait(0.5)

        print("\nAnalyzing your wordlists...")
        wordlist_dir = "./wordlists"
        
        # Vérification que le dossier existe
        if not os.path.isdir(wordlist_dir):
            print(f"Error: The directory '{wordlist_dir}' does not exist.")
            exit(1)

        # Lister les fichiers dans le dossier wordlists
        wordlists = [os.path.join(wordlist_dir, wordlist) for wordlist in os.listdir(wordlist_dir) if os.path.isfile(os.path.join(wordlist_dir, wordlist))]

        if not wordlists:
            print(f"Error: No wordlists found in '{wordlist_dir}' directory.")
            exit(1)

        wait(0.5)

        print("\nNumber of wordlists:", len(wordlists))
        for k, v in enumerate(wordlists):
            print(f"[{k+1}] {os.path.basename(v)}")

        # Choisir la wordlist
        try:
            w_choosed = input("Choose your wordlist [default = 1]: ").strip()
            w_choosed = int(w_choosed) - 1 if w_choosed.isdigit() else 0
            if not (0 <= w_choosed < len(wordlists)):
                raise ValueError
        except ValueError:
            print("Invalid choice! Using default wordlist.")
            w_choosed = 0

        print("\nChosen wordlist:", os.path.basename(wordlists[w_choosed]))

        print("\nTrust the script.")
        wait(0.5)

        if extract_eapol():
            if convert_in_hc22000():
                print("Crack will start...")
                wait(0.5)
                subprocess.run("clear", shell=True)
                wait(0.1)
                hashcat(wordlists, w_choosed)

    except Exception as e:
        print(f"Unexpected error: {e}")
