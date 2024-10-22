from sanic import Sanic
from sanic.response import html
from sanic.response import text
from sanic.request import Request
import sqlite3
import requests
import random
import json


app = Sanic("WordleCS")


@app.route("/")
async def index(request):
    file = open("index.html", "r")
    index = file.read()
    return html(index)




@app.route('/words', methods=["POST", "GET"],)
async def words(request: Request):

     if request.json == "cronjob":
         with open('words.json', 'r') as file:
            data = json.load(file)

         random.shuffle(data)

         with open('words.json', 'w') as file:
            json.dump(data, file, indent=4)

         return text("Words Randomised")
     else:
         with open('words.json', 'r') as file:
             data = file.read()

         return text(data)



# { request.json = e.g. '1':['a''u''d''i''o'] '2':['a''u''d''i''o'] '3':[] '4':[] '5':[]}
@app.route('/backend', methods=["POST"],)
async def backend(request: Request):
    return text(request.json)



