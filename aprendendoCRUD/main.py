from flask import Flask, render_template, flash, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.db'

db = SQLAlchemy(app)
class Estudantes(db.Model):
    id = db.Column('estudante_id', db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    email = db.Column(db.String(100))
    pin = db.Column(db.String(100))

    def __init__(self, nome, cidade, email, pin):
        self.nome = nome
        self.cidade = cidade
        self.email = email
        self.pin = pin

@app.route('/')
def show_all():
    return render_template('show_all.html', estudantes=Estudantes.query.all())

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cidade'] or not request.form['email'] or not request.form['pin']:
            flash('Preencha todos os campos', 'Erro')
        else:
            estudante = Estudantes(request.form['nome'], request.form['cidade'], request.form['email'], request.form['pin'])
            db.session.add(estudante)
            db.session.commit()
            flash('Estudante salvo', 'Sucesso')
            from flask import redirect
            return redirect(url_for('show_all'))
        return render_template('new.html')
if __name__ == 'main':
    app.app_context().push()
    db.create_all()
    app.run(host="0.0.0.0", port="5000", debug=True)