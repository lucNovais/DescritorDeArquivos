import os
import argparse

from datetime import datetime
from multiprocessing.pool import ThreadPool

def abrir_arquivo(caminhos):
    linhas = []
    for caminho in caminhos:
        with open(caminho) as arquivo:
            linhas.append(arquivo.readlines())

    retorno = []
    with ThreadPool() as pool:
        items = [(caminhos[i], linhas[i]) for i in range(len(caminhos))]
        for result in pool.starmap(pega_status, items):
            retorno.append(result)

    return retorno

def pega_status(caminho, linhas):
    stats_arquivo = os.stat(caminho)

    num_linhas = len(linhas)
    tamanho_bytes = stats_arquivo.st_size
    ultima_modificacao = datetime.fromtimestamp(stats_arquivo.st_mtime)

    return [num_linhas, tamanho_bytes, ultima_modificacao]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', metavar='F', type=str, nargs='+')

    args = parser.parse_args()
    
    caminhos = args.files
    
    info = abrir_arquivo(caminhos)

    for i in range(len(info)):
        print(f'\nInformacoes do arquivo {caminhos[i]}:')
        print(f'\tNumero de linhas: {info[i][0]}')    
        print(f'\tTamanho em bytes: {info[i][1]}')
        print(f'\tData de modificacao: {info[i][2]}\n')

if __name__ == '__main__':
    main()
