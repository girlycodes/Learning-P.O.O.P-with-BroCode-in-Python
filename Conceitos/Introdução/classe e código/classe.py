# Neste arquivo, escreveremos apenas a nossa classe!


class Carro: # a classe a ser criada deve sempre começar com letras maiúsculas  
    def __init__(self, cor, modelo, ano, está_vendendo): # dentre parênteses está os atributos que nossos objetos terão
        self.cor = cor # atribuindo nossos atributos
        self.modelo = modelo
        self.lili = ano # as variáveis não necessariamente precisam se chamar "self."nome do atributo", mas é recomendado para não lhe confundir enquanto coda
        self.está_vendendo = está_vendendo
    
    def acelerar(self):
        print("Esse carro consegue acelerar")
    def freiar(self):
        print("Esse carro consegue freiar")
    def serdirigido(self):
        print(f"Essa {self.modelo} é dirigido pelo João. O ano dele é de {self.lili}")