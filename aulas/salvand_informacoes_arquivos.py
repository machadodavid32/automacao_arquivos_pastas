"""
COMO CRIAR E MODIFICAR ARQUIVOS
'r' - usado somente para ler algo
'w' - Usado somente para escrever algo
'r+' - Usado para ler e escrever algo
'a' - Usado para acrescentar algo
    
"""


import os  # para usar o quebra linha os.linesep
"""
# COMO CRIAR UM ARQUIVO
with open('nomes.txt', 'w', newline='', encoding='utf-8') as arquivo:  
    # Aqui estamos criando um arquivo, primeiro vai o nome e depois o que iremos fazer w, r, r+, a
    arquivo.write('Olá, sou um arquivo'+os.linesep)
    
    # o 'w' sempre irá sobrescrever o arquivo anterior.
    
# Como adicionar um novo conteúdo sem apagar o anterior

with open('nomes.txt', 'a', newline='', encoding='utf-8') as arquivo:
    arquivo.write('Olá, sou uma nova linha'+os.linesep)  #os.linesep vai server como quebra de linha.
    
# Como ler um arquivo já criado

with open('nomes.txt', 'r', newline='', encoding='utf-8'):
    for linha in arquivo:
        print(linha)    
        
        
# Ler e acrescentar algo ao mesmo tempo
with open('nomes.txt', 'r+', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('Dev aprender' + os.linesep)
"""    
    
celulares = [860, 565, 457, 4567]
with open('celulares.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for valor in celulares:
        arquivo.write(str(valor)+os.linesep)  # converti para string    
                
# Como ler uma lista de dados
with open('celulares.txt', 'r', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
        
# para adicionar algo novo sem apagar o anterior
with open('celulares.txt', 'a', newline='', encoding='utf-8') as arquivo:
    arquivo.write('10000'+os.linesep)
    
# Para ler e escrever
with open('celulares.txt', 'r+', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('15000'+os.linesep)
                                    