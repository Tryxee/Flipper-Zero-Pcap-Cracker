from itertools import product, permutations
import time
import os
import sys

def generate_wordlist(words, output_file):
    start_time = time.time()
    unique_variations = set()

    try:
        # Charger les mots existants si le fichier existe
        if os.path.exists(output_file):
            with open(output_file, "r") as file:
                unique_variations = set(file.read().splitlines())

        with open(output_file, "a") as file:
            # Ajouter toutes les variations de chaque mot individuellement
            for word in words:
                print(f"Generation of variations for the word : {word}")
                variations = map("".join, product(*[(char.lower(), char.upper()) for char in word]))
                for variation in variations:
                    if variation not in unique_variations:
                        file.write(variation + "\n")
                        unique_variations.add(variation)

            # Ajouter toutes les combinaisons et permutations des mots concaténés
            for i in range(1, len(words) + 1):
                for combo in permutations(words, i):
                    combined_word = "".join(combo)
                    print(f"Generation of variations for the combination : {combined_word}")
                    variations = map("".join, product(*[(char.lower(), char.upper()) for char in combined_word]))
                    for variation in variations:
                        if variation not in unique_variations:
                            file.write(variation + "\n")
                            unique_variations.add(variation)

    except KeyboardInterrupt:
        print("\nEnd detected (Ctrl+C). Saving data.")

    end_time = time.time()
    print(f"Total words created and saved : {len(unique_variations)}")
    print(f"Duration : {end_time - start_time:.2f} secondes")

if __name__ == "__main__":

    try:
        file_name = str(input("Please enter the file name"))

        # Liste des mots fournis par l'utilisateur
        mots = input("Enter your words split by spaces : ").split()

        # Nom du fichier de sortie
        fichier_sortie = f"{file_name}.txt"

        # Génération de la wordlist
        generate_wordlist(mots, fichier_sortie)
        print(f"Wordlist generate and save in {fichier_sortie}.")

    except KeyboardInterrupt:
        print("\nEnd detected (Ctrl+C). Finished.")
