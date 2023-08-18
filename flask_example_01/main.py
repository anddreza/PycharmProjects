from flask import Flask

app = Flask(__name__)

# criar nosso index
@app.route("/")
def index():
    return "<h1>Index de teste</h1>"

#criar página de teste
@app.route("/teste")
def teste():
    return "<h1>Outra página de teste</h1>"

# função hello
@app.route("/hello")
@app.route("/hello")
@app.route("/hello/<nome>")
def hello(nome):
    return "<h2> Hello {}</h2>".format(nome)

@app.route("/debug")
def debug():
    return "<h1>Apresentando debug usando RULES</h1>"

app.add_url_rule("/debug", "Debug", debug)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
