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


class DataBase:

    def __init__(self):
        self.conexao = sqlite3.connect('basededados.db')
        self.cursor = self.conexao.cursor()

    def add_pessoas(self, pessoa: User):
        self.cursor.execute('INSERT INTO pessoas Values (nome:, idade:, cidade:)',
                            {'nome': pessoa.nome, 'idade': pessoa.idade, 'cidade': pessoa.cidade})

        self.conexao.commit()

        self.cursor.close()
        self.conexao.close()

    def ver_pessoas(self):
        self.conexao.commit()

        self.cursor.execute('SELECT * FROM pessoas')
        pessoas = []
        for linha in self.cursor.fetchall():
            pessoas.append(linha)

        self.cursor.close()
        self.conexao.close()

        return pessoas





