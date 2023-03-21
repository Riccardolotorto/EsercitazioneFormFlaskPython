from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home2.html')

@app.route('/login', methods = ["POST"])
def login():
    nome = request.form["nome"]
    password = request.form["password"]
    sesso = request.form["sesso"]
    if password != "123":
        if sesso == "Maschio":
            return render_template("login.html", saluto = "Benvenuto", utente = nome)
        elif sesso == "Femmina":
            return render_template("login.html", saluto = "Benvenuta", utente = nome)
        else:
            return render_template("login.html", saluto = "Ciao", utente = nome)
    else:
        return ("password errata")
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)