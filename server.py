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
    return html('<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Send Seqta Message</title><script src="https://cdn.tailwindcss.com"></script><script src="https://unpkg.com/htmx.org@2.0.3" integrity="sha384-0895/pl2MU10Hqc6jd4RvrthNlDiE9U1tWmX7WRESftEDRosgxNsQG/Ze9YMRzHq" crossorigin="anonymous"></script></head><body class="bg-gray-100 flex items-center justify-center h-screen"> <div class="max-w-md w-full p-6 bg-white rounded-md shadow-md"> <h2 class="text-2xl font-semibold text-gray-800 mb-6">Send Seqta Message</h2> <form action="/send" method="POST"> <div class="mb-4"> <label for="cookie" class="block text-gray-700 font-semibold mb-2">Your Cookie</label> <input type="text" id="cookie" name="cookie" placeholder="node04jzz3j3h4n4j3b4h4bh4b.node0" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500"> </div> <div class="mb-4"> <label for="id" class="block text-gray-700 font-semibold mb-2">Recipient ID</label> <input type="text" id="id" name="id" placeholder="1281" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500"> </div> <div class="mb-4"> <label for="subject" class="block text-gray-700 font-semibold mb-2">Subject</label> <input id="subject" name="subject" placeholder="Your subject/title here..." required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500"> </div> <div class="mb-6"> <label for="message" class="block text-gray-700 font-semibold mb-2">Message</label> <textarea id="message" name="message" rows="4" placeholder="Your message here..." required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500"></textarea> </div> <div> <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition duration-200">Send Message</button> </div> </form> </div></body></html>')


@app.route('/words', methods=["POST", "GET"],)
async def send(request: Request):

     if request.body == "cronjob":
         with open('words.json', 'r') as file:
            data = json.load(file)

         random.shuffle(data)

         with open('words.json', 'w') as file:
            json.dump(data, file, indent=4)

         return text("Words Randomised")
     else:
         with open('words.json', 'r') as file:
             data = json.load(file)

         return text(data)





