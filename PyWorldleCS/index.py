# Import all necessary modules and Packages
from wordle_module import getworldewords
from wordle_module import clear_terminal
from colorama import Fore, Back, Style, init
import pyfiglet


# Set up a basic code for variables and for managing colorama
init(autoreset=True)
wgs = -1
worddata = getworldewords(wgs)
v1 = 0
aft = 0

# Make a function that will serve as the start page to the Python app, telling users to press play to start the game or press C to close the game.
def startpage():
    i1wgs = -1
    wcs_1_big_text = pyfiglet.figlet_format("Wordle CS", font="slant")
    print(Fore.GREEN + Style.BRIGHT + wcs_1_big_text)
    print(Fore.GREEN + Style.BRIGHT + "Welcome to Wordle CS, the community made infinite wordle game.")
    print("[P]lay")
    print("[C]ose")
    kbp1 = input("Please choose your option, press the key and then press Enter")
    if kbp1 == "p":
        i1wgs = 0
    elif kbp1 == "c":
        i1wgs = -2
    else:
        print("Error with start page function")
    return i1wgs

def game():
   clear_terminal()
   if aft == 3:
       i2wgs = -2
   else:
       i2wgs = 0
   return i2wgs




while v1 == 0:

   #debug
   print(wgs)
   aft = aft +1
   print(aft)
   print(worddata)
   #debug

   if wgs >= 0:
       wsg = game()
   elif wgs == -1:
       wgs = startpage()
   elif wgs == -2:
       v1 = 1
   else:
       exit()
else:
    exit()





