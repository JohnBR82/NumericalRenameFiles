import os
import time
import sys
import ctypes
from colorama import init, Fore, Back, Style

# Inicializa o colorama para funcionar corretamente no Windows
init()

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    print(text.center(terminal_width))

def loading_animation(total, current, width=50):
    percent = current / total
    filled_width = int(width * percent)
    bar = '█' * filled_width + '-' * (width - filled_width)
    percent_display = f"{percent:.0%}"
    print(f"\r|{bar}| {percent_display}", end='', flush=True)

def rename_files(directory, prefix):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    total_files = len(files)

    clear_console()
    set_console_title("Renaming Files")
    print_centered("=== Renaming Files ===")
    print()

    for i, filename in enumerate(files, 1):
        base, extension = os.path.splitext(filename)
        new_name = f"{prefix}{i:03d}{extension}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        
        loading_animation(total_files, i)
        time.sleep(0.1) 

    print("\n\nRenaming completed!")

def main():
    clear_console()
    set_console_title("Numerical Rename File")

    ascii_art = r"""
 
                        ####                      
                    ############                  
                    ############                  
                    ####    ####                  
                    ############                  
                    ############                  
                      ######                      
                        ####                      
                        ####                      
                    ############                  
        ##          ############          ##      
      ######            ####            ######    
    ##########          ####          ##########  
    ##########          ####        ############  
      ######            ####          ########    
        ######          ####          ######      
          ####          ####        ######        
          ########      ####      ########        
            ########    ####    ########          
              ########################            
                  ################                
                                                  

 | \ | |                         (_)         | | |  __ \                                 |  ____(_) |     
 |  \| |_   _ _ __ ___   ___ _ __ _  ___ __ _| | | |__) |___ _ __   __ _ _ __ ___   ___  | |__   _| | ___ 
 | . ` | | | | '_ ` _ \ / _ \ '__| |/ __/ _` | | |  _  // _ \ '_ \ / _` | '_ ` _ \ / _ \ |  __| | | |/ _ \
 | |\  | |_| | | | | | |  __/ |  | | (__ (_| | | | | \ \  __/ | | | (_| | | | | | |  __/ | |    | | |  __/
 |_| \_|\__,_|_| |_| |_|\___|_|  |_|\___\__,_|_| |_|  \_\___|_| |_|\__,_|_| |_| |_|\___| |_|    |_|_|\___|

    """

    print(Fore.CYAN + ascii_art + Style.RESET_ALL)
    print_centered("Welcome to the Numerical Rename File!")
    print()

    directory = input("Enter the folder path: ")
    prefix = input("Enter the prefix for the files (leave blank to not use a prefix): ")

    if os.path.exists(directory):
        rename_files(directory, prefix)
    else:
        print(Fore.RED + "Directory not found!" + Style.RESET_ALL)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()