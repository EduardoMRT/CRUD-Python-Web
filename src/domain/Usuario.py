from src.domain.Pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome, idade, cpf, nomeUsuario, senha):
        super().__init__(nome, idade, cpf)
        self.nomeUsuario = nomeUsuario
        self.senha = senha

