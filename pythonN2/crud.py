import json

from flask import Flask, request, render_template, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import time
app = Flask(__name__, template_folder='public')
#URI para caminho até o banco de dados, se fosse um BD mais robusto ele teria uma string de conexão 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' #conexão com o banco de dados
db = SQLAlchemy(app)
# desde que você tem as classes relacionandas ao banco, o ORM faz o processo de criar, recuperar e converter
class Pessoas(db.Model):
    # definição dos tipos de dados do banco
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.Integer)
    observacao = db.Column(db.String(100))

    #objeto
    def __init__(self, nome, email, telefone, observacao):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.observacao = observacao
#serialização, se tiver problemas ao serializar em JSON os objetos, faça:
    def to_dict(self):
        return {
        'nome':self.nome,
        'email': self.email,
        'telefone': self.telefone,
        'observacao': self.observacao
        }


    @staticmethod
    def populate_db():
        lista_pessoas = []
        # Aqui estou criando 100 usuários, mas a ideia era ser 10k
        for i in range(100):
            lista_pessoas.append(Pessoas(
                nome='Usuario Teste',
                email='teste@gmail.com',
                telefone=i,
                observacao='i'))

        db.session.add_all(lista_pessoas)
        db.session.commit()

# verificação do tempo gasto para criar isso e alteração para json
@app.route('/')
def show_all():

    inicio = time.time()
    Pessoas.populate_db()

    pessoas = Pessoas.query.all()
    pessoas_to_dict = []
    for e in pessoas:
        pessoas_to_dict.append(e.to_dict())

    aux = json.dumps(pessoas_to_dict)

    fim = time.time()
    tempo = (fim - inicio) * 1000
    print(fim - inicio)
    return render_template('show_all.html', pessoas=aux, x=tempo)

if __name__ == '__main__':
    app.app_context().push() # recupera o contexto da aplicação que está usando o banco
    db.create_all() # cria todas as instâncias da database se não existirem
    app.run(host="0.0.0.0", port="5000", debug=True)
