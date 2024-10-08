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

def gameui(currentinputnumber, wordtoguess, guessedletters, wordsguessed):
    clear_terminal()
    print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("Wordle CS", font="slant"))
    print(wordsguessed[0])
    print(wordsguessed[1])
    print(wordsguessed[2])
    print(wordsguessed[3])
    print(wordsguessed[4])
    print(wordsguessed[5])
    return 1





def game():
    wordtoguess = getworldewords(wgs)
    currentinputnumber = 0
    v2 = 0
    i2wgs = -2
    guessedletters = []
    wordsguessed = ["[][][][][]", "[][][][][]", "[][][][][]", "[][][][][]", "[][][][][]", "[][][][][]"]
    # while v2 == 0:
    currentinputnumber = currentinputnumber + 1
    v2 = gameui(currentinputnumber, wordtoguess, guessedletters, wordsguessed)

    return i2wgs









if wgs >= 0:
    wsg = game()
elif wgs == -1:
   clear_terminal()
   wgs = startpage()
elif wgs == -2:
     v1 = 1
else:
  clear_terminal()
  exit()






