import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')
contador = 0

def formata_tamanho(tamanho):
    base = 1024
    kilo = base ** 2
    mega = base ** 3
    giga = base ** 4
    tera = base ** 5
    peta = base ** 6
    
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto /= 'T'
    else:
        tamanho /= peta
        texto = 'P'
        
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.',',')

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                
                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho do arquivo:', caminho_completo)
                print('Nome do arquivo:', nome_arquivo)
                print('Extensão do arquivo:', ext_arquivo)
                print('Tamanho do arquivo:', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem autorização para acessar o arquivo.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido:', e)
                
print()
print(f'{contador} arquivo(s) encontrado(s).')