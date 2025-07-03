# Demonstração de polimorfismo com classes que redefinem o método voar.
# - Passaro: classe base com método voar().
# - Pardal e Avestruz: subclasses que redefinem voar com comportamentos distintos.
# - Aviao: exemplo de herança imprópria — herda de Passaro apenas para reutilizar o método voar.
# - plano_voo(obj): aceita qualquer objeto com o método voar (polimorfismo).
# Exemplo:
#   plano_voo(Pardal())     -> "Pardal pode voar"
#   plano_voo(Avestruz())   -> "Avestruz não pode voar"
#   plano_voo(Aviao())      -> "Avião está decolando..."

# Classe base representando um pássaro genérico
class Passaro:
    def voar(self):
        print("Voando...")  # Comportamento genérico de voo


# Classe que herda de Passaro e especializa o método voar
class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")  # Comportamento realista


# Classe que herda de Passaro, mas não voa
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")  # Comportamento incompatível com a classe base


# EXEMPLO PROBLEMÁTICO: Avião herda de Passaro apenas para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")  # Avião não é um pássaro – má prática de herança


# Função que aceita qualquer objeto com método voar
def plano_voo(obj):
    obj.voar()  # Chama o método voar do objeto recebido


# Testes com as diferentes classes
plano_voo(Pardal())     # Pardal pode voar
plano_voo(Avestruz())   # Avestruz não pode voar
plano_voo(Aviao())      # Avião está decolando...
