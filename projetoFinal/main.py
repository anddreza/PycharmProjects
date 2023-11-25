from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# instancia da aplicação do Flask usando a pasta com arquivos HTML

app = Flask(__name__, template_folder="templates")
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.db' # conexao com o banco de dados
app.config['SECRET_KEY'] = "random string" # para criptografar as sessões


#criando a instancia do banco de dados
db = SQLAlchemy(app)
class Estudantes(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))
    email = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    # objeto
    def __init__(self, nome, cidade, email, pin):
        self.nome = nome
        self.cidade = cidade
        self.email = email
        self.pin = pin

# rota default (padrão) - lista todos os estudantes
@app.route('/')
def show_all():
    # renderiza os dados em tela
    return render_template('show_all.html', estudantes = Estudantes.query.all())

# Criando a rota para responder a solicitação de novos usuários
# Usaremos GET para quando tiver de madnar uma mensagem de erro
# Usaremos POST para salvar os addos no banco de dados, botão "confirmar"

@app.route('/new', methods=['GET', 'POST'])
def new_estudante():
    #verifica qual o tipo de requisição
    if request.method == 'POST': # codigo do post para verificar se os campos da tela foram preenchidos
        if not request.form['nome'] or not request.form['cidade'] or not request.form['email'] or not request.form['pin']:
            flash('Preencha todos os campos')
        else:
            #criar o objeto com as informações da tela
            estudante = Estudantes(request.form['nome'], request.form['cidade'], request.form['email'], request.form['pin'])
    #salvar no banco de dados
            db.session.add(estudante)
    #dar o comando de commit na database
            db.session.commit()
        # mensagem informativa de sucesso
        flash("Usuário cadastrado")
        return redirect(url_for('show_all'))

    #deixamos a chamada do render template para o final, de forma ao final de uma execução de função, será garantida a chamda de uma tela
    return render_template('new.html')

@app.route('/delete/<int:id>')
def delete(id):
    #criar um objeto a partir de registros no banco de dados
    #buscando pelo campo id
    estudante = Estudantes.query.get(id)

    #deletamos o objeto estudante
    db.session.delete(estudante)
    #commita as alterações no banco de dados
    db.session.commit()

    #informa que deletou o usuário
    flash('Usuario ' + estudante.nome + ', foi deletado!')
    return redirect(url_for('show_all'))


# update de estudante
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_estudante(id):

    estudante = Estudantes.query.get(id)

    if request.method == 'POST':  # codigo do post para verificar se os campos da tela foram preenchidos
        if not request.form['nome'] or not request.form['cidade'] or not request.form['email'] or not request.form['pin']:
            flash('Preencha todos os campos')
        else:
            # criar o objeto com as informações da tela
            estudante.nome = request.form['nome']
            estudante.cidade = request.form['cidade']
            estudante.email = request.form['email']
            estudante.pin  = request.form['pin']

            db.session.commit()
        # mensagem informtiva de sucesso
        flash("Usuário atualizado")
        return redirect(url_for('show_all'))

    return render_template('update.html', estudante = estudante)


if __name__ == '__main__':
    app.app_context().push() #criar o contexto da aplicação
    db.create_all() #cria todas as instancia da database se não existirem
    app.run(debug=True, host="0.0.0.0", port=5500) # inicia o server no modo debug
