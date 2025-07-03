# Exemplo de uso de classe abstrata com métodos e propriedade abstratos.
# - ControleRemoto (ABC): define interface com métodos ligar, desligar e a propriedade marca.
# - ControleTV e ControleArCondicionado: implementam completamente a interface da classe base.
# - Uso de @abstractmethod e @property garante que subclasses implementem os comportamentos obrigatórios.
# Exemplo:
#   controle = ControleTV()
#   controle.ligar()             # "Ligando a TV..."
#   print(controle.marca)        # "Philco"
# Importa recursos para criar classes e métodos abstratos
from abc import ABC, abstractmethod, abstractproperty

# Classe abstrata base para controles remotos
class ControleRemoto(ABC):
    # Método abstrato: deve ser implementado pelas subclasses
    @abstractmethod
    def ligar(self):
        pass

    # Método abstrato: deve ser implementado pelas subclasses
    @abstractmethod
    def desligar(self):
        pass

    # Propriedade abstrata: deve ser implementada pelas subclasses
    @property
    @abstractproperty
    def marca(self):
        pass


# Subclasse que representa um controle remoto de TV
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


# Subclasse que representa um controle remoto de Ar Condicionado
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


# Instancia um controle de TV e usa seus métodos
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

# Instancia um controle de ar-condicionado e usa seus métodos
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
