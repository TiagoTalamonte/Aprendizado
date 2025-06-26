nome = "TiAgO"  # Define uma variável chamada 'nome' com o valor "TiAgO"

print(nome.upper())  # Imprime o valor de 'nome' em letras maiúsculas: "TIAGO"
print(nome.upper())  # Repete a impressão do valor em maiúsculas
print(nome.upper())  # Repete novamente a impressão do valor em maiúsculas

texto = "  OLÁ MUNDO    "  # Define uma variável 'texto' com espaços no começo e no fim

print(texto)  # Imprime o texto exatamente como está, com espaços
print(texto.strip() + ".")  # Remove espaços no início e no fim e adiciona um ponto no final
print(texto.rstrip() + ".")  # Remove apenas os espaços à direita (fim) e adiciona um ponto
print(texto.lstrip() + ".")  # Remove apenas os espaços à esquerda (início) e adiciona um ponto

menu = "Python"  # Define a variável 'menu' com o valor "Python"

print("####" + menu + "####")  # Imprime "####Python####", concatenando strings com '#'
print(menu.center(14))  # Centraliza a palavra "Python" em uma largura de 14 caracteres, preenchendo com espaços
print(menu.center(14, "#"))  # Centraliza "Python" em 14 caracteres, preenchendo com '#' ao invés de espaços

print("P-y-t-h-o-n")  # Imprime a string exatamente assim, com hífens entre as letras

for letra in menu:  # Percorre cada letra da string 'menu'
    print(letra, end="-")  # Imprime cada letra seguida de um hífen, sem pular linha (end="-" mantém o cursor na mesma linha)
print()  # Dá uma quebra de linha depois do loop para organizar a saída

print("-".join(menu))  # Junta todas as letras da string 'menu', separando cada uma por um hífen
