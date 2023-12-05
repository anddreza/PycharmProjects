from flask import Flask, request, redirect, url_for, flash, render_template
import pymysql

connection = pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   database="comercio")

cursor = connection.cursor()
app = Flask(__name__, template_folder="templates")

def add_categorias(nome):
    cursor.execute("INSERT INTO categorias(Id, nome, id_categoria_pai, criado_em, alterado_em)"
                   "VALUES (DEFAULT, %s, DEFAULT, DEFAULT, DEFAULT)",
                   (nome))
    connection.commit()
    return 1

@app.route("/new_categorias", methods=["POST", "GET"])
def novacategoria():
    if request.method == "POST":
        if not request.form['nome']:
            flash('Preencha todos os campos')
        else:
            nome = request.form['nome']
            add_categorias(nome)
            return redirect(url_for('show_all_categorias'))
    else:
            return render_template('new_categorias.html')

@app.route("/select_categorias")
def show_all_categorias():
    resultvalue = cursor.execute("SELECT * FROM categorias")
    if resultvalue > 0:
        categorias = cursor.fetchall()
        print(categorias)
        return render_template('show_all_categorias.html', categorias=categorias)
    else:
        return render_template('show_all_categorias.html')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM categorias WHERE id = %s", (id))
    connection.commit()
    return redirect(url_for('show_all_categorias'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def updatecategorias(id):
    if request.method == "POST":
        if not request.form['nome']:
            flash('Preencha todos os campos')
        else:
            nome = request.form['nome']
            cursor.execute("UPDATE usuarios SET nome = %s WHERE id = %s",
                           (nome, id))
            connection.commit()
            return redirect(url_for('show_all_categorias'))
    else:
        cursor.execute("SELECT * FROM categorias WHERE id = %s", (id))
        result = cursor.fetchone()
        return render_template('update_categorias.html', categoria=result)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
