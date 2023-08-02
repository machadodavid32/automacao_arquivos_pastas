import os

# Exiba todos os arquivos da pasta desafio_arquivos
print(os.listdir())


# Monte e exiba o caminho(path) dos 3 arquivos desta pasta
print(os.path.join(os.getcwd() + os.sep + 'relatorio.pdf', 'datas_aniversario.xlsx', 'precos.txt'))


# Monte e exiba o caminho(path) que estão dentro das subpasta(desafios_texto)
texto_1 = os.getcwd() + os.sep + 'desafios_texto' + os.sep + 'desafio_texto1'
texto_2 = os.getcwd() + os.sep + 'desafios_texto' + os.sep + 'desafio_texto2'
texto_3 = os.getcwd() + os.sep + 'desafios_texto' + os.sep + 'desafio_texto3'

print(texto_1)
print(texto_2)
print(texto_3)
# Navegue para as 3 seguintes pastas, usando o os.chdir():

# pasta desafios_texto
os.chdir(os.getcwd() + os.sep + 'desafios_texto')

# de volta para a pasta desafios_arquivos
os.chdir(os.pardir)

    # Diretório pai da pasta desafio_arquivos
    
    