class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print("Som genérico de animal")

    def __str__(self):
        return f"{self.__class__.__name__}: " + ', '.join(f"{k}={v}" for k, v in self.__dict__.items())

# Subclasses que herdam de Animal
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

class Papagaio(Animal):
    def __init__(self, nome, especie, sabe_falar):
        super().__init__(nome, especie)
        self.sabe_falar = sabe_falar

    def falar(self):
        print("Olá! Eu sei falar!" if self.sabe_falar else "Squawk!")

# Criando objetos
dog = Cachorro("Rex", "Canino")
cat = Gato("Mimi", "Felino")
parrot = Papagaio("Loro", "Ave", True)

# Exibindo objetos
print(dog)
dog.fazer_som()

print(cat)
cat.fazer_som()

print(parrot)
parrot.falar()
