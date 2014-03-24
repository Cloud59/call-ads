from flask import Flask, request, render_template, g

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/control/')
def controller():
    return render_template('control.html')

if __name__ == '__main__':
    app.run(debug=True)
