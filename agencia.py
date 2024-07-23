from random import randint

class Agencia:

    def __init__(self,telefone,cnpj,numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print("Caixa abaixo do nível recomendado. Caixa atual: {}".format(self.caixa))
        else:
            print(f'O Valor do caixa esta ok. Caixa atual {self.caixa}')

    def emprestar_dinheiro(self,valor,cpf,juros):
        if self.caixa >valor:
            self.emprestimos.append((valor,cpf,juros))
            print('Emprestimo efetuado')
        else:
            print("Caixa insuficiente para efetuar o empréstimo solicitado.")
    
    def adicionar_clientes(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))


class AgenciaVirtual(Agencia):
    def __init__(self,site,telefone,cnpj,numero):
        self.site = site
        super().__init__(telefone,cnpj,numero)

class AgenciaComum(Agencia):
    def __init__(self,telefone,cnpj):
        super().__init__(telefone,cnpj,randint(1001,9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self,telefone,cnpj):
        super().__init__(telefone,cnpj,randint(1001,999))
        self.caixa = 50000000








agencia_virtual = AgenciaVirtual('www.',645626,645692,2458)
print(agencia_virtual.__dict__)