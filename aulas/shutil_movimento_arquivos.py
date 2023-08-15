import shutil
import os


"""
# Copiar de um lugar para outro
relatorio = os.getcwd() + os.sep + 'relatorio.pdf'
fotos = os.getcwd() + os.sep + 'fotos'
shutil.copy(relatorio, fotos)
"""
# Copiar uma pasta toda
caminho_pasta_musica = os.getcwd() + os.sep + 'musica'
fotos = os.getcwd() + os.sep + 'fotos'
shutil.copytree(caminho_pasta_musica, fotos, dirs_exist_ok=True)

