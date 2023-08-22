import shutil
import os


"""
# Copiar de um lugar para outro
relatorio = os.getcwd() + os.sep + 'relatorio.pdf'
fotos = os.getcwd() + os.sep + 'fotos'
shutil.copy(relatorio, fotos)
"""
# Copiar conteúdo de uma pasta para outra
caminho_pasta_musica = os.getcwd() + os.sep + 'musica'
fotos = os.getcwd() + os.sep + 'fotos'
#shutil.copytree(caminho_pasta_musica, fotos, dirs_exist_ok=True)

# copiar pasta e seus conteúdos para uma nova pasta.
os.makedirs('fotos' + os.sep + 'musica') # Criando a pasta musica dentro da pasta fotos
pasta_musica_em_pasta_fotos = os.getcwd() + os.sep + 'fotos' + os.sep + 'musica' # criando um caminho p/ pasta musica dentro da pasta fotos
shutil.copytree(caminho_pasta_musica, pasta_musica_em_pasta_fotos, dirs_exist_ok=True)

