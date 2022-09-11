from fastapi import FastAPI
from classes import User


app = FastAPI()


@app.post("/Pessoa")
def add_pessoa(nome: str, idade: int):
    usuario = User(nome, idade)



@app.get("/Pessoas")
def ver_pessoas():
    with open('Lista_Pessoas.txt', 'r') as arquivo:
        return arquivo.readlines()
