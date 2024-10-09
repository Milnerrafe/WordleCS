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
    print(f"var in startpage = {wgs}")
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
    inputselected = False
    wordinput = ""
    clear_terminal()
    print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("Wordle CS", font="slant"))

    if wordsguessed[0] == "null":
        if not inputselected:
            wordinput = input("[][][][][]")
            inputselected = True
        else:
            print("[][][][][]")
    else:
        print(wordsguessed[0])

    if wordsguessed[1] == "null":
        if not inputselected:
            wordinput = input("[][][][][]")
            inputselected = True
        else:
            print("[][][][][]")
    else:
        print(wordsguessed[1])

    if wordsguessed[2] == "null":
        if not inputselected:
            wordinput = input("[][][][][]")
            inputselected = True
        else:
            print("[][][][][]")
    else:
        print(wordsguessed[2])

    if wordsguessed[3] == "null":
        if not inputselected:
            wordinput = input("[][][][][]")
            inputselected = True
        else:
            print("[][][][][]")
    else:
        print(wordsguessed[3])

    if wordsguessed[4] == "null":
        if not inputselected:
            wordinput = input("[][][][][]")
            inputselected = True
        else:
            print("[][][][][]")
    else:
        print(wordsguessed[4])

    if wordsguessed[5] == "null":
        if not inputselected:
            wordinput = input("[][][][][]")
            inputselected = True
        else:
            print("[][][][][]")
    else:
        print(wordsguessed[5])

    return wordinput





def game():
    wordtoguess = getworldewords(wgs)
    currentinputnumber = 0
    v2 = 0
    i2wgs = -2
    guessedletters = []
    wordsguessed = ["AUDIO", "WORDS", "null", "null", "null", "null"]
    # while v2 == 0:
    currentinputnumber = currentinputnumber + 1
    wordinput = gameui(currentinputnumber, wordtoguess, guessedletters, wordsguessed)

    if wordsguessed[0] == "null":
        wordinput = wordsguessed[0]
    elif wordsguessed[1] == "null":
        wordinput = wordsguessed[1]
    elif wordsguessed[2] == "null":
        wordinput = wordsguessed[2]
    elif wordsguessed[3] == "null":
        wordinput = wordsguessed[3]
    elif wordsguessed[4] == "null":
        wordinput = wordsguessed[4]
    elif wordsguessed[5] == "null":
        wordinput = wordsguessed[5]

    print(wordsguessed)
    return i2wgs






wgs = startpage()
if wgs == 0:
    game()






