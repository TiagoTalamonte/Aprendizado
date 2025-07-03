# Classe Estudante com atributo de classe "escola" (compartilhado por todas as instâncias).
# - __init__: define nome e matrícula (atributos de instância).
# - __str__: retorna uma string formatada com os dados do estudante.
# - mostrar_valores(*objs): imprime a representação de cada objeto.
# Mudança no atributo de classe afeta todas as instâncias (até mesmo as criadas antes).
# Exemplo:
#   aluno_1 = Estudante("Guilherme", 1)
#   aluno_2 = Estudante("Giovanna", 2)
#   Estudante.escola = "Python"
#   aluno_3 = Estudante("Chappie", 3)
#   mostrar_valores(aluno_1, aluno_2, aluno_3)

# Define a classe Estudante com um atributo de classe
class Estudante:
    escola = "DIO"  # Atributo de classe compartilhado entre todas as instâncias

    def __init__(self, nome, matricula):
        self.nome = nome            # Atributo de instância
        self.matricula = matricula  # Atributo de instância

    # Método que define a representação em string do objeto (usado por print)
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


# Função que recebe múltiplos objetos e os imprime
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)  # Chama o __str__ de cada objeto


# Criação de dois estudantes
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

# Mostra os valores dos dois estudantes (escola ainda é "DIO")
mostrar_valores(aluno_1, aluno_2)

# Altera o valor do atributo de classe 'escola'
Estudante.escola = "Python"

# Cria novo estudante após a alteração da escola
aluno_3 = Estudante("Chappie", 3)

# Mostra os valores de todos os estudantes após a mudança da escola
mostrar_valores(aluno_1, aluno_2, aluno_3)
