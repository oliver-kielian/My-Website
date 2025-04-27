import os
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'mycoolawesomekey'
CORS(app)

@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")

@app.route('/art', methods=["GET"])
def art():
     return render_template("art.html")

@app.route('/game', methods=["GET"])
def game():
     return render_template("game.html")

@app.route('/game/claw_machine', methods=["GET"])
def claw_machine():
    return render_template("index.html")

@app.route('/static/game/<path:filename>')
def serve_game_assets(filename):
    if filename.endswith('.wasm'):
        return send_from_directory(os.path.join(app.root_path, 'static', 'game'), filename, mimetype='application/wasm')
    return send_from_directory(os.path.join(app.root_path, 'static', 'game'), filename)

@app.route('/game/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(os.path.join(app.root_path, 'game', 'assets'), filename)

@app.route('/contact', methods={"GET", "POST"})
def contact():
     if request.method == "GET":
          return render_template("contact.html")
     else:
          return 0

if __name__ == '__main__':
     app.run(debug=True)