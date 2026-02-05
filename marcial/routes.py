from flask import render_template, url_for, redirect, session, request, flash

import csv

import os

from marcial import app




@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login')
def login ():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST'])
def autenticar_login():
    email_digitado = request.form['email']
    cpf_digitado = request.form['cpf']

    caminho_arquivo = os.path.join('data' , 'cadastros.csv')
    usuario_existente = False
                                                                                                                                                                                                                                                                                

    with open(caminho_arquivo, mode= 'r' , newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)

        for linha in leitor:
            email_salvo = linha[1]
            cpf_salvo = linha[2]

            if email_salvo == email_digitado and cpf_salvo == cpf_digitado:
                usuario_existente == True
                break
    if usuario_existente:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
@app.route("/cadastro_usuario")
def cadastro():

    plano_selecionado = request.args.get('plano')

    if plano_selecionado:
        nome_plano = plano_selecionado.capitalize()
        id_plano = plano_selecionado
    else:
        nome_plano = "nennhum"
        id_plano = ''

   
    

    return render_template('cadastro.html', nome_plano = nome_plano, plano_id = id_plano)

@app.route('/cadastro', methods =['POST'])
def salvar_cadastro():
    nome = request.form['nome_usuario']
    email = request.form['email']
    cpf = request.form['cpf']
    plano = request.form['plano_final']

    if usuario_existente(cpf , email):

        flash('CPF ou email existente')
        
        return redirect(url_for('cadastro', plano=plano))
    
    sexo = request.form['sexo']
    modalidade = request.form['modalidade']
    

    dados = [nome , email , cpf , sexo , modalidade , plano]

    caminho_arquivo = os.path.join('data', 'cadastros.csv')


    with open(caminho_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(dados)   
    
    return redirect(url_for('home'))

def usuario_existente(cpf , email):

    caminho_arquivo = os.path.join('data', 'cadastros.csv')

    if not os.path.exists(caminho_arquivo):
        return False
    
    with open(caminho_arquivo , mode ='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)

        for linha in leitor:
            email_existe = linha[1]
            cpf_existe = linha[2]

            if cpf_existe == cpf or email_existe == email:
                return True
    
    return False


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route("/boxe")
def boxe():
    return render_template("boxe.html")


@app.route("/jiu-jitsu")
def jj():
    return render_template("jj.html")

@app.route("/judo")
def judo():
    return render_template("judo.html")

@app.route("/thai")
def thai():
    return render_template("thai.html")