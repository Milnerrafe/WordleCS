from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    index_html = open("index.html")
    return index_html

@app.route('/htmx/button_1', methods=['GET', 'POST'])
def button_1():
    button_1 = '<div class="text-2xl font-mono hover:font-serif hover:text-blue-600 text-gray-950 ">WOW</div>'
    return button_1



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
