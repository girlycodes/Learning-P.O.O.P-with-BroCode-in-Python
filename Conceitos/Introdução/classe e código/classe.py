# Neste arquivo, escreveremos apenas a nossa classe!


class Carro: # o nome da classe a ser criada deve sempre começar com letras maiúsculas  
    def __init__(self, cor, modelo, ano, está_vendendo): # aqui estamos criando os atributos; dentre parênteses estão os atributos que nossos objetos terão
        
        self.cor = cor # atribuindo o atributo cor, abaixo, os demais atributos estão sendo atribuídos
        self.modelo = modelo
        self.lili = ano # as variáveis não necessariamente precisam se chamar "self."nomedoparâmetro", mas é recomendado para não nos confundir
        self.está_vendendo = está_vendendo
    
    def acelerar(self):
        print("Esse carro consegue acelerar")
    def freiar(self):
        print("Esse carro consegue freiar")
    def serdirigido(self):
        print(f"Esse carro {self.modelo} é dirigido pelo João. O ano dele é de {self.lili}")