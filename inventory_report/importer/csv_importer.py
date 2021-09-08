import importer.py
import csv
from pathlib import Path

class CsvImporter(Importer):
    def __init__(self, arquivo)
    super.arquivo = arquivo

    def import_data():
        leituraArquivo = dict()
        if Path(caminho).suffix == '.csv':
            with open(caminho) as csv_file:
        
                csv_reader = csv.reader(csv_file, delimiter=',')

                csv_reader.__next__()

                for row in csv_reader:
                    leituraArquivo.append({
                        "id": {row[0]},
                        "nome_do_produto": {row[1]},
                        "nome_da_empresa": {row[2]},
                        "data_de_fabricacao": {row[3]},
                        "data_de_validade": {row[4]},
                        "numero_de_serie": {row[5]},
                        "instrucoes_de_armazenamento": {row[6]}
                    })
            return leituraArquivo
        else:
            return("Extensão do arquivo inválido")
