# Import all necessary modules and Packages
from wordle_module import getworldewords
from wordle_module import clear_terminal
from colorama import Fore, Back, Style, init
import pyfiglet

# Set up a basic code for variables and for managing colorama
init(autoreset=True)
worddata = getworldewords(0)


big_text = pyfiglet.figlet_format("Wordle CS", font="slant")
print(Fore.GREEN + Style.BRIGHT + big_text)


print("WordleCS")
print("world")
print(Fore.RED + Back.YELLOW + Style.BRIGHT + 'Red text with yellow background and bright style')


# Initialize colorama






