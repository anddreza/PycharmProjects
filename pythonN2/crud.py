from flask import Flask, request, render_template, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import time
app = Flask(__name__, template_folder='public')
##URI para caminho até o banco de dados, se fosse um BD mais robusto ele teria uma string de conexão 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

class Pessoas(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.Integer)
    observacao = db.Column(db.String(100))

    def __init__(self, nome, email, telefone, observacao):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.observacao = observacao

    @staticmethod
    def populate_db():
        lista_pessoas = []
        for i in range(100):
            lista_pessoas.append(Pessoas(
                nome='Rishkan',
                email='New York',
                telefone=i,
                observacao='i'))

        db.session.add_all(lista_pessoas)
        db.session.commit()

    @staticmethod
    def toJSON():
        print(db.session.query(Pessoas).all())
        return db.session.query(Pessoas).all()


@app.route('/success/<tempo>')
def success(tempo):
    print(jsonify(Pessoas.toJSON()))
    return 'Tempo: %s' %tempo

@app.route('/adicionaPessoas')
def tempo():
    inicio = time.time()
    Pessoas.populate_db()
    fim = time.time()
    tempo = (fim - inicio) * 1000
    print(fim - inicio)
    return redirect(url_for('success', tempo=(fim - inicio) * 1000))


if __name__ == '__main__':
    app.app_context().push() # recupera o contexto da aplicação que está usando o banco
    db.create_all() # cria todas as instâncias da database se não existirem
    app.run(host="0.0.0.0", port="5000", debug=True)
    #Pessoas.populate_db()

    # @app.route('/new', methods=['GET', 'POST'])
    # def new():
    #     if request.method == 'POST':
    #         if not request.form['nome'] or not request.form['email'] or not request.form['telefone'] or not request.form['observacao']:
    #             flash('Preencha todos os campos', 'Erro')
    #         else:
    #             estudante = Pessoas(request.form['nome'], request.form['email'], request.form['telefone'], request.form['observacao'])
    #             db.session.add(pessoas)
    #             db.session.commit()
    #             flash('Usuário salvo!', 'Sucesso')
    #             from flask import redirect
    #             return redirect(url_for('show_all'))
    #         return render_template('new.html')
    #
    # app.add_url_rule("/debug", "Debug", debug)