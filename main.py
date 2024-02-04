import pathlib
from pathlib import Path
import os
from colorama import Fore
import sys

def main():
    if len(sys.argv) < 2:
        adress = ''
    else:
        input = sys.argv[1]
        adress= pathlib.Path(input)

    try:
        for child in pathlib.Path(adress).glob('**/*'):
            if os.path.isdir(child):
                print(f"{Fore.BLUE} [FOLDER] {Path(child).name} {Fore.RESET}")
            else:
                print(f"{Fore.RED} [FILE] {Path(child).name} {Fore.RESET}")

    except:
        print("Wrong adress")

if __name__ == '__main__':
    main()