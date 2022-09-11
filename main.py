from fastapi import FastAPI
from classes import User
import sqlite3



app = FastAPI()

conexao = sqlite3.connect('database.db', check_same_thread=False)
cursor = conexao.cursor()


@app.post("/Pessoa")
def add_pessoa(nome: str, idade: int, cidade: str):
    usuario = User(nome, idade, cidade)

    cursor.execute('INSERT INTO pessoas (nome, idade, cidade) Values (:nome, :idade, :cidade)',
                        {'nome': usuario.nome, 'idade': usuario.idade, 'cidade': usuario.cidade})
    conexao.commit()


@app.post("/Deletar pessoas")
def deletar_pessoas(id:str):
    cursor.execute('DELETE FROM pessoas WHERE id=:id', {'id':id})



@app.get("/Pessoas")
def ver_pessoas():
    conexao.commit()
    
    cursor.execute('SELECT * FROM pessoas')
    pessoas = [linha for linha in cursor.fetchall()]

    return pessoas
