from flask import Flask, request, render_template, redirect, url_for
from ordenacao import sorting
import time, timeit
import random

app = Flask(__name__, template_folder='public')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/success/<name><tempo>')
def success(name, tempo):
    return 'Ordenado: %s %s' % (name, tempo)


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


#
# any_numbers = request.form.get('ordenacao')
#        # any_numbers_list = any_numbers.split(",")
#         any_numbers_list = (list(map(int, any_numbers.split(","))))
#        #any_numbers = random.sample(range(1, 100), 42)
#         sorting.quicksort(any_numbers_list)
#         print(any_numbers_list)
#         return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
