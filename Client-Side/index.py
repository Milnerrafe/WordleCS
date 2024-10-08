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
    clear_terminal()
    i1wgs = -1
    print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("Wordle CS", font="slant"))
    print(Fore.GREEN + "Welcome to Wordle CS, the community made infinite wordle game.")
    print(Fore.YELLOW + Style.BRIGHT + "[P]lay ")
    print(Fore.RED + Style.BRIGHT + "[C]ose")
    kbp1 = input(Fore.BLUE + "Please choose your option, press the key and then press Enter↵")
    if kbp1 == "p":
        clear_terminal()
        i1wgs = 0
    elif kbp1 == "c":
        clear_terminal()
        i1wgs = -2
    else:
        print("Error with start page function")
    return i1wgs

def game():
   clear_terminal()
   c1 = 0
   v2 = 0
   word1 = " █ █ █ █ █ █ █"
   word2 = " █ █ █ █ █ █ █"
   word3 = " █ █ █ █ █ █ █"
   word4 = " █ █ █ █ █ █ █"
   word5 = " █ █ █ █ █ █ █"
   word6 = " █ █ █ █ █ █ █"
   while v2 == 0:
       i2wgs = 0
       print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("Wordle CS", font="slant"))
       print(word1)
       print(word2)
       print(word3)
       print(word4)
       print(word5)
       print(word6)
       if c1 == 1:
           word1 = input(f"Enter Your Guess, Number {c1}")
       elif c1 == 2:
           word2 = input(f"Enter Your Guess, Number {c1}")
       elif c1 == 3:
           word3 = input(f"Enter Your Guess, Number {c1}")
       elif c1 == 4:
           word4 = input(f"Enter Your Guess, Number {c1}")
       elif c1 == 5:
           word5 = input(f"Enter Your Guess, Number {c1}")
       elif c1 == 6:
           word6 = input(f"Enter Your Guess, Number {c1}")
       c1 = c1 + 1
       if c1 == 6:
           v2 = 1
   if v2 == 2:
       i2wgs = -1
   return i2wgs




while v1 == 0:

   #debug
   print(f"debug wgs={wgs}, aft={aft}, worddata={worddata}. ")
   aft = aft +1
   #debug

   if wgs >= 0:
       wsg = game()
   elif wgs == -1:
       clear_terminal()
       wgs = startpage()
   elif wgs == -2:
       v1 = 1
   else:
       # for prod clear_terminal()
       exit()
else:
    # for prod clear_terminal()
    exit()





