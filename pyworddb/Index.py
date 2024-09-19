## Here we import all the Python packages that we'll need to make this code work.
import json
import random
from datetime import datetime

## Here we declare the variables that we'll need to use so that the variables exist when we want to change them.
ranworddata = '0'
date = '0'

## Here we get the date and format it.
current_date = datetime.now()
formatted_date = current_date.strftime('%d/%m/%y')
date = formatted_date

## Here we declare the JSON data
json_data = '''
{
    "words": ["gnome", "audio"]
}
'''

## Here we randomise the JSON data and declare it as a global variable.
def ranworddatamake():
    global ranworddata
    data = json.loads(json_data)
    random.shuffle(data['words'])
    ranworddata = json.dumps(data, indent=4)

## Here we check if our time database JSON file exists. If it does, then we read it and remove any excess spaces.If it doesn't exist, then we set it to a variable with no data inside, so the next piece of code will be able to create it with the correct date.
try:
    with open("datedatabase.json", "r") as datedatabase:
        saved_date = datedatabase.read().strip()
except FileNotFoundError:
    saved_date = ''


if saved_date == date:
    with open("index.json", "w") as index_file:
        index_file.write(ranworddata)
else:
    with open("datedatabase.json", "w") as datedatabase:
        datedatabase.write(date)

    ranworddatamake()

    with open("index.json", "w") as index_file:
        index_file.write(ranworddata)
