# Variáveis Globais
# São variáveis definidas fora de todas as funções, no nível do módulo (arquivo).
# Estão disponíveis em todo o código, dentro e fora das funções — desde que você as chame corretamente.
# Por padrão, você só pode ler o valor global dentro de uma função, a menos que use a palavra-chave global para modificar.

# Váriaveis Locais
# São variáveis definidas dentro de uma função.
# Só existem e podem ser usadas dentro dessa função.
# Cada vez que a função é chamada, as variáveis locais são criadas e depois destruídas.


#  Variável global
pontos = 0

def ganhar_pontos(valor):
    #  Indicamos que queremos usar a variável global
    global pontos
    pontos += valor
    print(f"[FUNÇÃO] Ganhou {valor} pontos! Total agora: {pontos}")

def mostrar_pontos():
    # Aqui apenas acessamos (não precisamos de 'global' se só vamos ler)
    print(f"[FUNÇÃO] Pontuação atual: {pontos}")

def resetar_pontos():
    #  Variável local: diferente da global
    pontos = 0
    print(f"[FUNÇÃO] Pontos resetados localmente para: {pontos}")

#  Uso real
print(f"[GLOBAL] Pontos iniciais: {pontos}")
ganhar_pontos(10)
mostrar_pontos()

resetar_pontos()  # Isso não afeta a variável global
mostrar_pontos()  # Ainda mostra o valor global real
