from flask import Flask, request, redirect, url_for, flash, render_template
import pymysql

connection = pymysql.connect(host="127.0.0.1",
                   user="root",
                   password="Bosonhiggs99!",
                   database="ecommerce")

cursor = connection.cursor()
app = Flask(__name__, template_folder="templates")


def add_text(email, nome, sobrenome):
    cursor.execute("INSERT INTO usuarios(ID, email, nome, sobrenome, ativo, criado_em, alterado_em)"
                   "VALUES (DEFAULT, %s, %s, %s, DEFAULT, DEFAULT, DEFAULT)",
                   (email, nome, sobrenome))
    connection.commit()
    return 1


@app.route("/new", methods=["POST", "GET"])
def novousuario():
    if request.method == "POST":
        if not request.form['email'] or not request.form['nome'] or not request.form['sobrenome']:
            flash('Preencha todos os campos')
        else:
            email = request.form['email']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            add_text(email, nome, sobrenome)
            return redirect(url_for('show_all'))
    else:
        return render_template('new.html')


@app.route("/usuarios", methods=['GET'])
def show_all():
    resultvalue = cursor.execute("SELECT * FROM usuarios")
    if resultvalue >= 0:
        usuarios = cursor.fetchall()
        return render_template('show_all.html', usuarios=usuarios)
    else:
        return render_template('new.html')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id))
    result_delete = cursor.fetchone()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id))
    connection.commit()

    print(result_delete)
    return render_template('show_all.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def updateusuario(id):
    if request.method == "POST":
        if not request.form['email'] or not request.form['nome'] or not request.form['sobrenome']:
            flash('Preencha todos os campos')
        else:
            email = request.form['email']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            cursor.execute("UPDATE usuarios SET email = %s, nome = %s, sobrenome = %s WHERE id = %s",
                           (email, nome, sobrenome, id))
            connection.commit()
            return redirect(url_for('show_all'))
    else:
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id))
        result = cursor.fetchone()
        print(result)
        return render_template('update.html', usuario=result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)