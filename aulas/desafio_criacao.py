import os

# Criar as listas a seguir
frutas = ['maça','banana', 'pera', 'kiwi', 'limao']
cores = ['branco', 'vermelho','preto','azul','amarelo']
programacao = ['python','javascript','c','java','PHP']

# Criar arquivo frutas.txt
with open('frutas.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta+os.linesep)

# imprimir na tela frutas.txt
with open('frutas.txt', 'r', newline='', encoding='utf-8') as arquivo:
    for fruta in arquivo:
        print(fruta)        

# Sem apagar os dados que já estão no arquivo frutas.txt adicione todas as cores da lista de cores para o arquivo frutas.txt

with open('frutas.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for cor in cores:
        arquivo.write(cor+os.linesep)
        


# Criar um arquivo linguagens.txt e popule o arquivo de modo que cada linguagem popule uma linha

with open('linguagens.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for linguagem in programacao:
        arquivo.write(linguagem+os.linesep)
                
        