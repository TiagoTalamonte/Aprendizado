# Reutilizar código (sem duplicação)
# Organizar melhor o sistema
# Especializar comportamentos (sobrescrevendo métodos)
# Herdará todos os métodos e atributos públicos da superclasse
# Pode adicionar novos métodos
# Pode sobrescrever métodos existentes (redefinir o comportamento)


class Animal:
    def __init__(self, nome):
        self.nome = nome
        print(f" Animal '{self.nome}' criado.")

    def emitir_som(self):
        print(" Som genérico de animal.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama o construtor da classe pai
        self.raca = raca
        print(f" Cachorro da raça {self.raca} criado.")

    def emitir_som(self):
        print(" Au au!")

# Uso prático
animal1 = Animal("Bicho-preguiça")
animal1.emitir_som()

print("-----")

dog1 = Cachorro("Bolt", "Labrador")
dog1.emitir_som()
