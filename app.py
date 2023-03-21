#Scrivere una web app che calcoli l'area del quadrato o del rettangolo in base alla scelta dell'utente tramite un menù a tendina. Fare tutto ciò con le funzioni
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/risultato', methods = ["GET"])
def risultato():
    figura = request.args.get("area")
    base = int(request.args.get("base"))
    altezza = int(request.args.get("altezza"))
    def area(base, altezza):
        return base * altezza
    if figura == "quadrato":
        return render_template('risultato.html', figura = figura, valoreArea = area(base, altezza))
    else:
        return render_template('risultato.html', figura = figura, valoreArea = area(base, altezza))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)