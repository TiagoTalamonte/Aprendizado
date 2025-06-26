frutas = ['Limão', 'Uva', 'Laranja']
curso = "Curso de Python"
outra_lista = frutas
nova_lista = ['Limão', 'Uva', 'Laranja']

# Associação (verifica conteúdo)
print('Laranja' in frutas)           
print('Maçã' not in frutas)           
print('Python' in curso)              
print('python' in curso)              

# Identidade (verifica se são o MESMO objeto na memória)
print(frutas is outra_lista)          
print(frutas is nova_lista)           
print(frutas is not nova_lista)       
