from pydantic import BaseModel


class User():
    def __init__(self, nome: str, idade: str):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade
