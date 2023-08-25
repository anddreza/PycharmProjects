from flask import Flask, request

app = Flask(__name__, static_folder='public')

# criar nosso index
@app.route("/add", methods=["POST", "GET"])
def add():
   if(request.method == "POST"):
       usuario = request.form['nome']
       senah = request.form['senha']
   elif request.method == "GET":
       return "ok - GET"

if __name__ == '__main__':
    app.run(debug=True, port=3000)