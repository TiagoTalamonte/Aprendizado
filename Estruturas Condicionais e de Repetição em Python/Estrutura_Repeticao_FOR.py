texto = input("Informe seu texto: ")

vogais = "AEIOUÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙ"

quantidade_vogais = 0  # Contador

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
        quantidade_vogais += 1

print()  # quebra de linha
print(f"\nTotal de vogais encontradas: {quantidade_vogais}")

## Exemplo com Range

for numero in range (0, 51, 5):
    print(numero, end=" ")
