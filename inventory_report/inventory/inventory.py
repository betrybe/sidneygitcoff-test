import csv
import json
import xmltodict
import xml.etree.ElementTree as ET
from pathlib import Path
import "../reports/simple_report.py"
import "../reports/complete_report.py"

class Inventory:

    def import_data(simples = "", completo = ""):
        if simples != "":
            caminho = simples
        else:
            caminho = completo
        
        leituraArquivo = dict()

        if Path(caminho).suffix == '.csv':
        
            leituraArquivo = dict()
            
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

        elif Path(caminho).suffix == ".json":

            with open(caminho) as f:
                entrada = json.load(f)

            leituraArquivo = {campo:[] for campo in campos}

            for elemento in entrada:
                for campo in campos:
                    leituraArquivo[campo].append(elemento[campo])
        else:
            tree = ET.parse(caminho)
            leituraArquivo = xmltodict.parse(tree)

    

        if simples != "":
            SimpleReport.generate(leituraArquivo)
        else:
            CompleteReport.generate(leituraArquivo)
