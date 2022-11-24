"""
Dado um diretório na variável 'src_folder', o script navega por todos os arquivos e todas
as subpastas deste diretório e cria uma lista com todos os arquivos que são duplicados.
O checksum MD5 vai determinar se um arquivo é duplicado ou não.
"""

import os
import hashlib
from collections import defaultdict
import csv

src_folder = ".../.../..." # Pasta raíz onde a checagem vai iniciar


def generate_md5(fname, chunk_size=1024):
    """
    Função que pega um nome de um arquivo e retorna checksum MD5 deste arquivo
    """
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        # Lê o primeiro bloco do arquivo
        chunk = f.read(chunk_size)
        # Continua lendo o arquivo até o final e atualiza o hash quando acabar
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    # Retorna o checksum
    return hash.hexdigest()


if __name__ == "__main__":
    """
    Início do script
    """

    # Dicionário de valores, como lista
    md5_dict = defaultdict(list)

    # Tipos de arquivos para a checagem
    file_types_inscope = ["ppt", "pptx", "pdf", "txt", "html",
                          "mp4", "jpg", "jpeg", "png", "xls", "xlsx",
                          "xml", "vsd", "py", "json", "docx", "xlsx",
                          "xls", "eml", "zip", "rar", "mpeg", "mp3", "txt",
                          "doc", "ofx", "ico", "exe", "msi"
                          ]

    # Navega por todas as subtastas e arquivos dentro do diretório informado
    for path, dirs, files in os.walk(src_folder):
        print("Analisando {}".format(path))
        for each_file in files:
            if each_file.split(".")[-1].lower() in file_types_inscope:
                # A variável do diretório atualiza para cada subpasta
                file_path = os.path.join(os.path.abspath(path), each_file)
                # Se existem outros arquivos com o mesmo checksum, adiciona pra lista
                md5_dict[generate_md5(file_path)].append(file_path)

    # Identifica os checksum's contendo mais de um valor (nomes de arquivos)
    duplicate_files = (
        val for key, val in md5_dict.items() if len(val) > 1)

    # Abre e escreve a lista de arquivos duplicados em um arquivo CSV
    with open("duplicates.csv", "w", newline='', encoding='UTF-8') as log:
        # Terminador de linha adicionado pra Windows, senão ele insere linhas em branco...
        csv_writer = csv.writer(log, quoting=csv.QUOTE_NONE, delimiter=",", lineterminator="\n", escapechar="\'")
        header = ["Nomes dos arquivos"]
        csv_writer.writerow(header)

        for file_name in duplicate_files:
            csv_writer.writerow(file_name)

    print("Concluído")