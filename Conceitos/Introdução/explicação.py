# Objetos: Um conjunto de atributos (similares a funções com variáveis dentro e utilizados para descrever o que o objeto tem) e métodos (funções) relacionados
#     Exemplo: Objeto "celular" pode ter como atributos a sua versão e cor, enquanto como método a sua capacidade de fazer chamadas telefônicas e acender a lanterna.

# Precisamos de uma classe para criar objetos
#    Classes: são como "Blueprints" para projetar a estrutura e o layout de um objeto

# Veja agora uma classe com o objeto do exemplo, veja a seguir:

class Celular():
    def __init__(self, versão, cor ): # aqui estamos usando o construtor "def __init__(self)" para assumir os atributos do objeto "celular"
        self.versão = versão # para atribuir esses atributos, usamos "self.nomedoatributo", que será igual ao "nomedoatributo"
        self.cor = cor

    def fazerligações(self):
        print("Esse celular consegue fazer ligações")

    def ligarlanterna(self):
        print("Esse celular consegue ligar a  lanterna")

celular1 = Celular(13, "Branco")
print(celular1)  # esse comando apenas nos dá o endereço de memória do objeto "celular1"

# para  acessarmos alguns dos atributos desse  celular, usaremos o operador de acesso a atributos, que se baseia em:
print(celular1.versão) # o nome do nosso objeto seguido de um ponto, que é seguido do nome do atributo que queremos acessar
print(celular1.cor) # com esses dois comandos, será printado no terminal o número "13" e a palavra "Branco"

#agora, vamos printar os métodos do objeto
celular1.fazerligações() # o nome do nosso objeto seguido de um ponto seguido do nome do método executará o código escrito nesse método 
celular1.ligarlanterna()

# Como pode ver, é um pouco bagunçado escrever nossas classes e códigos num arquivo só, por isso, no arquivo seguinte, usaremos POO com dois arquivos diferentes.