from app import app
from flask import render_template, url_for, request

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
def novapagina():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print(pesquisa)
        context.update({'pesquisa':pesquisa})
    if request.method == 'POST':
        pesquisa = request.form['pesquisa']
        print('POST',pesquisa)
        context.update({'pesquisa':pesquisa})
    return render_template('contato.html',context=context)