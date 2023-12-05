from flask import Flask, request, redirect, url_for, flash, render_template
import pymysql

connection = pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   database="comercio")

cursor = connection.cursor()
app = Flask(__name__, template_folder="templates")

def add_produtos(Cod_barras, Nome, Descricao, status_produto, Preco_normal, Preco_com_desconto, Quantidade):
    cursor.execute("INSERT INTO produtos(Id, Cod_barras, Nome, Descricao, id_status_produto, Preco_normal, Preco_com_desconto, Quantidade, criado_em, alterado_em) "
                   "VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT)",
                   (Cod_barras, Nome, Descricao, status_produto, Preco_normal, Preco_com_desconto, Quantidade))
    connection.commit()
    return 1

@app.route("/new_products", methods=["POST", "GET"])
def novoproduto():
    if request.method == "POST":
        print(request.form)
        if not request.form['Cod_barras'] or not request.form['Nome'] or not request.form['Descricao']  \
                or not request.form['Preco_normal'] or not request.form['Quantidade']:
            flash('Preencha todos os campos')
        else:
            Cod_barras = request.form['Cod_barras']
            Nome = request.form['Nome']
            Descricao = request.form['Descricao']
            status_produto = request.form['status_produto']
            Preco_normal = request.form['Preco_normal']
            Preco_com_desconto = request.form['Preco_com_desconto']
            Quantidade = request.form['Quantidade']
            add_produtos(Cod_barras, Nome, Descricao, status_produto, Preco_normal, Preco_com_desconto, Quantidade)
            return redirect(url_for('show_all_produtos'))
    else:
        cursor.execute("SELECT Id, Nome FROM status_produtos")  # Ativo = 1 , Inativo = 2
        result = cursor.fetchall()
        return render_template('new_produtos.html', status=result)

@app.route("/products")
def show_all_produtos():
    resultvalue = cursor.execute("SELECT * FROM produtos")
    if resultvalue > 0:
        produtos = cursor.fetchall()
        print(produtos)
        return render_template('show_all_produtos.html', produtos=produtos)
    else:
        return render_template('show_all_produtos.html')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id))
    connection.commit()
    return redirect(url_for('show_all_produtos'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def updateprodutos(id):
    if request.method == "POST":
        if not request.form['Cod_barras'] or not request.form['Nome'] or not request.form['Descricao'] \
                or not request.form['Preco_normal'] or not request.form['Quantidade']:
            flash('Preencha todos os campos')
        else:
            Cod_barras = request.form['Cod_barras']
            Nome = request.form['Nome']
            Descricao = request.form['Descricao']
            status_produto = request.form['status_produto']
            Preco_normal = request.form['Preco_normal']
            Preco_com_desconto = request.form['Preco_com_desconto']
            Quantidade = request.form['Quantidade']
            cursor.execute("UPDATE produtos SET Cod_barras = %s, Nome = %s, Descricao = %s, id_status_produto = %s, Preco_normal = %s,"
                           "Preco_com_desconto = %s, Quantidade = %s WHERE id = %s",
                           (Cod_barras, Nome, Descricao, status_produto, Preco_normal, Preco_com_desconto, Quantidade, id))
            connection.commit()
            return redirect(url_for('show_all_produtos'))
    else:
        cursor.execute("SELECT * FROM produtos WHERE id = %s", (id))
        result = cursor.fetchone()
        cursor.execute("SELECT Id, Nome FROM status_produtos")  # Ativo = 1 , Inativo = 2
        resulta = cursor.fetchall()

        return render_template('update_produtos.html', produto=result, status=resulta)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
