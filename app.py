from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contatos = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    contatos.append(contato)
    return redirect('/')

@app.route('/contatos')
def lista_contatos():
    return render_template('contatos.html', contatos=contatos)

@app.route('/edit/<int:index>', methods=['GET'])
def edit(index):
    contato = contatos[index]
    return render_template('edit.html', contato=contato)

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    contatos[index] = contato
    return redirect('/')



if __name__ == '__main__':
    app.run()