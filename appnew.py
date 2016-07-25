from flask import Flask, render_template, json, request,redirect,session,jsonify, url_for

from werkzeug.wsgi import LimitedStream

#mysql = MySQL()
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('signin.html')


@app.route('/showIndex')
def showIndex():
    return render_template('index.html')


        

     


if __name__ == "__main__":
    app.run(debug=True)
