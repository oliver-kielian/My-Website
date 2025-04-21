from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'mycoolawesomekey'

@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")

@app.route('/art', methods=["GET"])
def art():
     return render_template("art.html")

@app.route('/game', methods=["GET"])
def game():
     return render_template("game.html")

@app.route('/contact', methods={"GET", "POST"})
def contact():
     if request.method == "GET":
          return render_template("contact.html")
     else:
          return 0

if __name__ == '__main__':
     app.run(debug=True)