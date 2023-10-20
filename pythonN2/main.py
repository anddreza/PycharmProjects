from flask import Flask, request, render_template, redirect, url_for
from ordenacao import sorting
import random
app = Flask(__name__, template_folder='public')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'Ordenado: %s' % name

@app.route("/rotaOrdenacao", methods=['GET', 'POST'])
def ordenacao():
   if request.method == 'POST':
       any_numbers = request.form.get('ordenacao')
       # any_numbers_list = any_numbers.split(",")
       any_numbers_list = (list(map(int, any_numbers.split(","))))
       # any_numbers = random.sample(range(1, 100), 42)
       sorting.quicksort(any_numbers_list)
       print(any_numbers_list)
       return redirect(url_for('success', name=any_numbers_list))
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