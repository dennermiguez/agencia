from datetime import datetime
import pytz
from random import randint


class Conta_corrente:

    def __init__(self, nome, cpf, agencia, conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agengia = agencia
        self._conta = conta
        self._transacoes = []
        self._cartoes = []

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%m:%S')

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))
        pass

    def depositar_dinheiro(self, valor):
        self._saldo += valor
        self._transacoes.append(
            (valor, self._saldo, Conta_corrente._data_hora()))
        pass

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para finalizar essa operação')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append(
                (valor, self._saldo, Conta_corrente._data_hora()))
        pass

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def consultar_historico(self, transacoes):
        print('Histórico de transações:')
        for transacao in self._transacoes:
            print(transacao)
        pass

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append(
            (-valor, self._saldo, Conta_corrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append(
            (valor, conta_destino.saldo, Conta_corrente._data_hora()))


class CartaoCredito:

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}{}'.format(
            CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = "{}{}{}".format(
            randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = None
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida")
