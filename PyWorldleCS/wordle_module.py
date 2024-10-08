import requests
import os


def getworldewords(wordnumber):
    if wordnumber > 3563:
        raise ValueError("Error: word number too high. Please pick a number between 0 and 3,563.")
    else:
        datafromurl = requests.get('http://wordlecs-server.rafemedia.com/')
        jsondata = datafromurl.json()["words"]
        return jsondata[wordnumber]


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def iswordreal(word):
    datafromurl = requests.get('http://wordlecs-server.rafemedia.com/')
    jsondata = datafromurl.json()["words"]
    wordlist = jsondata
    if word in wordlist:
        result = True
    else:
        result = False

    return result

