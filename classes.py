import sqlite3


class User:
    def __init__(self, nome: str, idade: int, cidade: str):
        self._nome = nome
        self._idade = idade
        self._cidade = cidade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def cidade(self):
        return self._cidade





