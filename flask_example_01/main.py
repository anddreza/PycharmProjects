from flask import Flask, redirect

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
def hello(nome="nao veio falor"):
    return "<h2> Hello {}</h2>".format(nome)

# url dinamica
@app.route("/user")
@app.route("/user/<int:userId>")
def user(userId = 0):
    if userId == 0:
        return "<h1> Usuário não informado</h1>"
    else:
        return "<h1> Usuário: {}</h1>".format(userId)

@app.route("/google")
def direct_example():
    return redirect("http://google.com")


@app.route("/redirect/hello")
def direct_example():
    return redirect("/hello")

@app.route("/debug")
def debug():
    return "<h1>Apresentando debug usando RULES</h1>"

app.add_url_rule("/debug", "Debug", debug)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
