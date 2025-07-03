# Classe Pessoa com métodos especiais:
# - __init__: inicializa nome e idade.
# - @classmethod criar_de_data_nascimento: cria Pessoa com base no ano de nascimento.
# - @staticmethod e_maior_idade: verifica se a idade >= 18.
# Exemplo:
#   p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
#   print(p.nome, p.idade)               # Guilherme 28
#   print(Pessoa.e_maior_idade(18))     # True
#   print(Pessoa.e_maior_idade(8))      # False

# Define a classe Pessoa com nome e idade
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # Atributo de instância
        self.idade = idade    # Atributo de instância

    # Método de classe usado como fábrica (factory method)
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano     # Calcula idade com base no ano de nascimento
        return cls(nome, idade)  # Cria e retorna uma instância de Pessoa

    # Método estático que verifica se a idade é maior ou igual a 18
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# Cria um objeto Pessoa usando o método de classe
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")

# Exibe o nome e idade da pessoa
print(p.nome, p.idade)  # Guilherme 28

# Usa o método estático para verificar maioridade
print(Pessoa.e_maior_idade(18))  # True
print(Pessoa.e_maior_idade(8))   # False
