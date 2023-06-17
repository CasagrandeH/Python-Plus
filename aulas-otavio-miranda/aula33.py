'''#metodo para criar arquivo + escrever nele

try:
    file = open('abc.txt', 'w+')
    file.write('Lmao\n')
    file.write('Lmaoo\n')
    file.write('Lmaooo\n')

    #metodos para ler arquivos

    file.seek(0, 0)
    print('Lendo as linhas do arquivo abc.txt:')
    print()
    print(file.read())

    file.seek(0, 0)
    print(f'Lendo linha por linha:')
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')

    file.seek(0, 0)
    print(f'Lendo como lista:')
    for lines in file.readlines():
        print(f'{lines}', end='')

#sempre fechar arquivo pois pode dar problema
finally:
    file.close()'''
    
#Metodo 'Pythonico' de fazer tudo que foi feito acima

with open('abc.txt', 'w+') as file:
    file.write(f'LMAO\n')
    file.write(f'LMAOO\n')
    file.write(f'LMAOOO\n')
    file.write(f'LMAOOOO\n')
    
    file.seek(0)
    print(file.read(), end='')
    
#(w+) escreve mas apagaa conteudo previo. (r) só lê o conteudo. (a+) escreve e não apaga conteudo previo. 'https://docs.python.org/3/library/functions.html#open' para esclarecimento sobre as funçoes
    
with open('abc.txt', 'a+') as file:
    file.write('GET FECKED\n')
    
    file.seek(0)
    print(file.read())