from flask import Flask

app = Flask(__name__)

@app.route('/c1', methods=['GET', 'POST'])
def c1():
    a = '<button class="big-button bg-blue-500 text-white hover:bg-blue-600 focus:outline-none" hx-post="http://127.0.0.1:5555/c2" hx-trigger="click" hx-swap="outerHTML" > You Clicked Me! </button>'
    return a


@app.route('/c2', methods=['GET', 'POST'])
def c2():
    a = ' <button class="big-button bg-blue-500 text-white hover:bg-blue-600 focus:outline-none" hx-post="http://127.0.0.1:5555/c1" hx-trigger="click" hx-swap="outerHTML" > Click Me! </button>'
    return a

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
