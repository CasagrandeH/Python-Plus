import os 
import shutil

caminho_original = 'C:/Users/User/Programas-e-Repositórios/repositorios-terceiros/knightin-clan-master'
novo_caminho = 'aulas-otavio-miranda/pasta'

#Criar uma pasta

try:
    os.mkdir(novo_caminho)
except FileExistsError as e:
    pass

#Copiar arquivos(se quiser mover arquivos é so trocar 'copy' por 'move' na função da linha 19)

'''for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(novo_caminho, file)
        
        shutil.copy(old_file_path, new_file_path)
        print(f'Arquivo {file} copiado com sucesso.')'''
        
#Apagar arquivos
        
for root, dirs, files in os.walk(novo_caminho):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(novo_caminho, file)
        
        os.remove(new_file_path)
        print(f'O arquivo {file}  foi apagado com sucesso')