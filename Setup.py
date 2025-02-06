import os
import subprocess
from time import sleep as wait

def Verify_Python():
    python_installed = input("\nPython is installed? (y/N): ").strip().lower()

    if python_installed in ["yes", "y", "true"]:
        pip_installed = input("\nPip is installed? (y/N): ").strip().lower()
        if pip_installed in ["yes", "y", "true"]:
            return True
        else:
            print("\nPip is required. Please install it! Exiting...")
            wait(2)
            return False
    elif python_installed in ["no", "n", "false"]:
        print("\nPython is required. Please install it! Exiting...")
        wait(2)
        return False
    else:
        print("Invalid input! Exiting...")
        wait(1.5)
        return False

def Install_Requirements():
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False

def Verify_Hashcat():
    main_dir = "./"

    try:
        for folder in os.listdir(main_dir):
            folder_path = os.path.join(main_dir, folder)

            if os.path.isdir(folder_path) and "hashcat" in folder.lower():
                print(f"\n{folder_path} Found!")
                return True
        
        print("\nNo hashcat folder found!")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def Try_Install_Hashcat():
    try:
        subprocess.run("clear", shell=True)
        print("\nTrust me")
        print("\nTrying to install Hashcat, please wait...")
        wait(1.5)
        subprocess.run("clear", shell=True)

        cmd = "cd ./bin && git clone https://github.com/hashcat/hashcat.git && cd ./hashcat && make && cd ../../"
        subprocess.run(cmd, shell=True, check=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing Hashcat: {e}")
        return False

if __name__ == "__main__":
    try:
        subprocess.run("clear", shell=True)
        print("Hello!")
        print("\nChecking if Python is installed...\n")
        wait(0.5)

        if Verify_Python():
            print("\nInstalling requirements...\n")
            wait(0.5)

            if Install_Requirements():
                print("\nRequirements installed. Checking if Hashcat is present...\n")
                wait(0.5)

                if not Verify_Hashcat():
                    print("\nHashcat not found. Attempting installation...\n")
                    wait(0.5)

                    if Try_Install_Hashcat():
                        print("\nInstallation successful! Launching Main.py...")
                        wait(1.5)
                        subprocess.run("clear && python Main.py", shell=True)
                else:
                    print("\nEverything is set! Launching Main.py...")
                    wait(1.5)
                    subprocess.run("clear && python Main.py", shell=True)
    except Exception as e:
        print(f"Error: {e}")
