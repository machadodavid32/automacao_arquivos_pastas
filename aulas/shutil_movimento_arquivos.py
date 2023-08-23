import shutil
import os


"""
# Copiar de um lugar para outro
relatorio = os.getcwd() + os.sep + 'relatorio.pdf'
fotos = os.getcwd() + os.sep + 'fotos'
shutil.copy(relatorio, fotos)
"""
"""
# Copiar conteúdo de uma pasta para outra
caminho_pasta_musica = os.getcwd() + os.sep + 'musica'
fotos = os.getcwd() + os.sep + 'fotos'
shutil.copytree(caminho_pasta_musica, fotos, dirs_exist_ok=True)
"""

"""
# copiar pasta e seus conteúdos para uma nova pasta.
os.makedirs('fotos' + os.sep + 'musica') # Criando a pasta musica dentro da pasta fotos
pasta_musica_em_pasta_fotos = os.getcwd() + os.sep + 'fotos' + os.sep + 'musica' # criando um caminho p/ pasta musica dentro da pasta fotos
shutil.copytree(caminho_pasta_musica, pasta_musica_em_pasta_fotos, dirs_exist_ok=True)
"""

"""
# Mover um arquivo individual para outro diretório
relatorio = os.getcwd() + os.sep + 'relatorio.pdf'
pasta_musica = os.getcwd() + os.sep + 'musica'
shutil.move(relatorio, pasta_musica)  # passando caminho inicial e diretório final
"""


"""
# Remover um diretório inteiro
pasta_musica = os.getcwd() + os.sep + 'musica'
shutil.rmtree(pasta_musica)
"""

# Zipar um diretório
fotos = os.getcwd() + os.sep + 'fotos'
#shutil.make_archive('zip codigo', 'zip', fotos) # primeiro passar o nome do arquivo, depois passar o formato e depois qual pasta será compactada
#shutil.make_archive('zip codigo_total', 'zip', os.getcwd()) # neste caso ele vai zipar todo o diretório

# Descompactando uma pasta
shutil.unpack_archive(os.getcwd() + os.sep + 'zip codigo.zip', 'codigo') # Passar o caminho pro diretorio atual + os.sep + nome do arquivo...
#... + a pasta onde deseja descompactar. Neste caso, a palavra 'codigo' é o destino final e também é uma nova pasta criada.


