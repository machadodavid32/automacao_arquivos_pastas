import os
"""
#os.mkdir('musica')  # Cria diretório

#os.makedirs('musica' + os.sep + 'rock') # cria um subdiretório

# para verificar se a pasta(diretório) ja existe, faça abaixo:

try:
    if not os.path.isdir('Musica'):
        os.mkdir('Musica')
    else:
        print('Diretório já foi criado')

except OSError:
    print('Não foi possivel criar diretório, pois já existe')
"""    
    
#DESAFIO    
os.makedirs('musica' + os.sep + 'Arqvuios')     
os.makedirs('Arqvuios' + os.sep + 'Arquivos pdf')          