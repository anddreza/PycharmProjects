from flask import Flask, request, debug
from ordenacao import quickSort

app = Flask(__name__, static_folder='public')

# criar nosso index
@app.route("/")
def index():
    return "<h1>Index de teste</h1>"

#criar página de teste
@app.route("/rotaOrdenacao", methods=['GET', 'POST'])
def ordenacao():
   if request.method == 'POST':
        ordenacao = request.form.get('ordenacao')
        quickSort.quickSort()


app.add_url_rule("/debug", "Debug", debug)

if __name__ == '__main__':
    app.run(debug=True, port=3000)