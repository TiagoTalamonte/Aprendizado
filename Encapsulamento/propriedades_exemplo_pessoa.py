# Classe Pessoa armazena nome e ano de nascimento.
# - Atributos:
#   - nome: nome da pessoa (público).
#   - _ano_nascimento: ano de nascimento (protegido).
# - Propriedade:
#   - idade: calcula a idade com base no ano atual (2022).
# Exemplo:
#   pessoa = Pessoa("Guilherme", 1994)
#   print(pessoa.nome)   # "Guilherme"
#   print(pessoa.idade)  # 28

# Define a classe Pessoa com nome e ano de nascimento
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome                      # Atributo público
        self._ano_nascimento = ano_nascimento  # Atributo protegido (por convenção)

    # Propriedade somente leitura que calcula a idade
    @property
    def idade(self):
        _ano_atual = 2022                     # Ano fixo para o exemplo
        return _ano_atual - self._ano_nascimento  # Calcula idade com base no ano de nascimento


# Cria uma instância da classe Pessoa
pessoa = Pessoa("Guilherme", 1994)

# Exibe o nome e a idade calculada
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
