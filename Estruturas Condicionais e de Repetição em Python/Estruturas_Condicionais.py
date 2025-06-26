maior_idade = 18
idade_especial = 70

idade = int(input("Informe sua idade: "))

# if idade >= maior_idade:
#     print("Maior de idade, pode tirar CNH.")

# if idade < maior_idade:
#     print("Ainda não pode tirar CNH")


# if idade >= maior_idade:
#     print("Maior de idade, pode tirar CNH.")
# else:
#     print("Ainda não pode tirar a CNH.")

if idade >= idade_especial:
    print("Muito velho para tirar carta")
elif idade >= maior_idade:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar a CNH.")