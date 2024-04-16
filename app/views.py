from app import app, db
from flask import render_template, url_for, request
from app.forms import contatoForm

@app.route('/')
def homepage():
    usuario = 'Fabiano'
    idade = 34

    context = {
        'usuario':usuario,
        'idade':idade
    }

    return render_template('index.html', context=context)

@app.route('/contato/',methods=['GET', 'POST'])
def contato():
    form = contatoForm()    
    context = {}
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
        )

        db.session.add(contato)
        db.session.commit()

    return render_template('contato.html',context=context, form=form)


    # if request.method == 'GET':
    #     pesquisa = request.args.get('pesquisa')
    #     print(pesquisa)
    #     context.update({'pesquisa':pesquisa})
    # if request.method == 'POST':
    #     pesquisa = request.form['pesquisa']
    #     print('POST',pesquisa)
    #     context.update({'pesquisa':pesquisa})
    # return render_template('contato.html',context=context)