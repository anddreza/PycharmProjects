from flask import Flask, request, render_template, redirect, url_for
from ordenacao import sorting
import time
import random

app = Flask(__name__, template_folder='public')
# A rota inicial, ela carrega a primeira informação que está cadastrada no index.html
@app.route("/")
def index():
    return render_template('index.html')
# A rota de sucesso mostrando o nome e tempo
@app.route('/success/<name><tempo>')
def success(name, tempo):
    return 'Ordenado: %s %s' % (name, tempo)

# A rota de ordenação onde acontece to-das as coisas, inclusive o time, e também onde faz o código de ordenação
# passa para ser mostrado
@app.route("/rotaOrdenacao", methods=['GET', 'POST'])
def ordenacao():
    if request.method == 'POST':
        any_numbers = request.form.get('ordenacao')
        # any_numbers_list = any_numbers.split(",")
        any_numbers_list = (list(map(int, any_numbers.split(","))))
        # any_numbers = random.sample(range(1, 100), 42)
        inicio = time.time()
        sorting.quicksort(any_numbers_list)
        print(any_numbers_list)
        fim = time.time()
        print(fim - inicio)
        return redirect(url_for('success', name=any_numbers_list, tempo=(fim - inicio)*1000))
    elif request.method == 'GET':
        return render_template('index.html')

# a porta
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
