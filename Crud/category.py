from flask import Flask, request, redirect, url_for, flash, render_template
import pymysql

connection = pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   database="comercio")

cursor = connection.cursor()
app = Flask(__name__, template_folder="templates")

def add_categorias(nome, id_categoria_pai):
    cursor.execute("INSERT INTO categorias(Id, nome, id_categoria_pai, criado_em, alterado_em)"
                   "VALUES (DEFAULT, %s, %s, DEFAULT, DEFAULT)",
                   (nome, id_categoria_pai))
    connection.commit()
    return 1

@app.route("/new_categorias", methods=["POST", "GET"])
def novacategoria():
    if request.method == "POST":
        if not request.form['nome']:
            flash('Preencha todos os campos')
        else:
            nome = request.form['nome']
            id_categoria_pai = request.form['id_categoria_pai']
            add_categorias(nome, id_categoria_pai)

            return redirect(url_for('show_all_categorias'))
    else:
        cursor.execute("SELECT Id, Nome FROM categorias")  # Ativo = 1 , Inativo = 2
        result = cursor.fetchall()
        return render_template('new_categorias.html', categorias=result)

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
            id_categoria_pai = request.form['id_categoria_pai']
            cursor.execute("UPDATE categorias SET nome = %s, id_categoria_pai = %s  WHERE id = %s",
                           (nome, id_categoria_pai, id))
            connection.commit()
            return redirect(url_for('show_all_categorias'))
    else:
        cursor.execute("SELECT * FROM categorias WHERE id = %s", (id))
        result = cursor.fetchone()
        cursor.execute("SELECT Id, Nome FROM categorias")
        resulta = cursor.fetchall()
        return render_template('update_categorias.html', categoria=result, categorias=resulta)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
