# Já neste, escreveremos nossos códigos para usarmos nossa classe

from classe import Carro # é asssim que importamos a classe de outro arquivo " from "nomedoarquivo" import "nome da classe" "

carro1 = Carro("Laranja", "Mercedes", 2025, False) # esses são os atributos do nosso objeto "carro1"
print(carro1.cor) # assim printamos no terminal o atributo "cor" desse objeto

carro1.acelerar() # assim executamos o código dentro do nosso método "acelerar"
carro1.serdirigido() # assim executamos o código dentro do nosso método "serdirigido"


carro2 = Carro("Azul escuro", "Ford", 2021, True) # esses são os atributos do nosso objeto "carro2"
print(carro2.está_vendendo) # assim printamos no terminal o atributo "está_vendendo" desse objeto

carro2.freiar() # assim executamos o código dentro do nosso método "freiar"
carro2.serdirigido() # assim executamos o código dentro do nosso método "serdirigido"