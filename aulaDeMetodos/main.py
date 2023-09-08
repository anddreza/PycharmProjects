from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder='public')

# criar nosso index
@app.route("/add", methods=["POST", "GET"])
def add():
   if(request.method == "POST"):
       # primeira forma
       usuario = request.form['nome']
       senha = request.form['senha']
       print(usuario)
       print(senha)

       # segunda forma
       data = request.form
       u2 = data['nome']
       s2 = data['senha']

       #terceir forma
       js = dumps(request.form)
       return js



   elif request.method == "GET":
       return "ok - GET"

if __name__ == '__main__':
    app.run(debug=True, port=3000)