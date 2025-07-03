# Classe Foo usa propriedades para encapsular acesso ao atributo _x.
# - __init__(x): inicializa _x com valor (ou None).
# - @property x: retorna _x ou 0 se for None.
# - @x.setter: soma valor ao _x.
# - @x.deleter: redefine _x para 0.
# Exemplo de uso:
#   foo = Foo(10)
#   print(foo.x)  # 10
#   del foo.x     # _x vira 0
#   print(foo.x)  # 0
#   foo.x = 10    # _x vira 10
#   print(foo.x)  # 10

# Define a classe Foo com encapsulamento e propriedades personalizadas
class Foo:
    def __init__(self, x=None):
        self._x = x  # Atributo "protegido" (por convenção, com underline)

    # Getter para a propriedade 'x'
    @property
    def x(self):
        # Retorna o valor de _x ou 0 se _x for None ou 0 (falsy)
        return self._x or 0

    # Setter para a propriedade 'x'
    @x.setter
    def x(self, value):
        # Soma o novo valor ao valor atual de _x
        self._x += value

    # Deleter para a propriedade 'x'
    @x.deleter
    def x(self):
        # Redefine _x para zero
        self._x = 0


# Cria um objeto Foo com valor inicial 10
foo = Foo(10)

# Imprime o valor atual (getter): 10
print(foo.x)

# Deleta a propriedade x (reseta para 0 usando o deleter)
del foo.x

# Imprime o novo valor de x: 0
print(foo.x)

# Usa o setter para somar 10 ao valor atual (0 + 10)
foo.x = 10

# Imprime o novo valor de x: 10
print(foo.x)
