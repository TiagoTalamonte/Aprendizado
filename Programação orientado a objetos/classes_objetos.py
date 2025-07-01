# Organização: Agrupa dados (atributos) e comportamentos (métodos) relacionados.
# Reutilização: Você cria a classe uma vez, pode fazer muitos objetos diferentes sem repetir código.
# Manutenção: Facilita modificar o comportamento de todos os objetos editando só a classe.
# Representação do mundo real: Você modela coisas reais (pessoas, carros, contas bancárias) de forma natural.

class Carro:
    def __init__(self, marca, modelo, ligado=False):
        print(" Inicializando o carro...")
        self.marca = marca
        self.modelo = modelo
        self.ligado = ligado

    def __del__(self):
        print(f" Carro {self.marca} {self.modelo} removido da memória.")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f" {self.marca} {self.modelo} está agora ligado!")
        else:
            print(f" {self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f" {self.marca} {self.modelo} foi desligado.")
        else:
            print(f" {self.marca} {self.modelo} já está desligado.")

def criar_carro():
    carro_temp = Carro("Fiat", "Uno", True)
    print(f" Carro criado: {carro_temp.marca} {carro_temp.modelo}")

# Uso principal
carro1 = Carro("Toyota", "Corolla")
carro1.ligar()

print(" Programa em execução...")

del carro1  # Força chamada ao destrutor

print(" Fim do programa.")

# criar_carro()  # Teste de instância temporária
