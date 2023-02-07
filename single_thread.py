import os
import argparse

from datetime import datetime

def abrir_arquivo(caminho):
    with open(caminho) as arquivo:
        linhas = arquivo.readlines()

    stats_arquivo = os.stat(caminho)

    num_linhas = len(linhas)
    tamanho_bytes = stats_arquivo.st_size
    ultima_modificacao = datetime.fromtimestamp(stats_arquivo.st_mtime)

    return [num_linhas, tamanho_bytes, ultima_modificacao]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', metavar='F', type=str)

    args = parser.parse_args()
    
    caminho = args.file
    
    info = abrir_arquivo(caminho)

    print(f'\nInformacoes do arquivo {caminho}:')
    print(f'\tNumero de linhas: {info[0]}')    
    print(f'\tTamanho em bytes: {info[1]}')
    print(f'\tData de modificacao: {info[2]}\n')

if __name__ == '__main__':
    main()
