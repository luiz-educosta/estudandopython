# Classes com atributo privado
class Lampada():
    
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def ligada(self):
        return self.__ligada
    

class Acesso():
    
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

# Classes com atributo publico
class ContaCorrente:
    
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


user = Acesso('luiz@inatel.br', '1234')



class Produto():

    # Atributo de classe
    imposto = 1.05 # imposto em cima do produto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1          # atributo de instância
        self.nome = nome                        # atributo de instância
        self.descricao = descricao              # atributo de instância
        self.valor = (valor * Produto.imposto)  # atributo de instância
        Produto.contador = self.id              # atributo de classe

p1 = Produto('Mochila', 'Mochila de montanha', 2000.0)
p2 = Produto('SmartWatch', 'Relógio de corrida', 2000.0)

print(p1.valor)
print(Produto.imposto)

print(p1.id)
print(p2.id)

# Criando um atributo dinâmico

p2.peso = '5kg'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Preço: {p2.valor}, Peso: {p2.peso}')


print(p2.__dict__)

# Deletando atributos

del p2.peso

# posso também fazer a seguinte remoção tbm

# del p2.valor
# del p2.descricao

print(p2.__dict__)

"""
7h50m

1h aula 115
"""   