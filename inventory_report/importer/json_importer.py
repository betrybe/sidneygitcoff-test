import importer.py
from pathlib import Path
import json

class JasonImporter(Importer):
    def __init__(self, arquivo)
    super.arquivo = arquivo

    def import_data():
        leituraArquivo = dict()
        if Path(caminho).suffix == ".json":

            with open(caminho) as f:
                entrada = json.load(f)

            leituraArquivo = {campo:[] for campo in campos}

            for elemento in entrada:
                for campo in campos:
                    leituraArquivo[campo].append(elemento[campo])
            return leituraArquivo
        else:
            return("Extensão do arquivo inválido")