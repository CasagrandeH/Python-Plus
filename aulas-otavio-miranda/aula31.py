import os

caminho_procura = 'aulas-otavio-miranda'
termo_procura = 'aula'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
        tamanho = os.path.getsize(caminho_completo)
        print(caminho_completo, nome_arquivo, tamanho, sep=' --- ')