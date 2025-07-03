#__init__Serve para inicializar o objeto, configurando seus atributos com valores iniciais.
#__del__ __del__ é para limpeza de recursos que o objeto pode estar usando, como arquivos abertos, conexões de rede 
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        print(f"Pessoa {self.nome} criada.")

    def __del__(self):
        print(f"Pessoa {self.nome} destruída (removida da memória).")

# Criando um objeto
p = Pessoa("João")

print("Fazendo outras coisas...")

# Apagando o objeto explicitamente
del p

print("Fim do programa.")
