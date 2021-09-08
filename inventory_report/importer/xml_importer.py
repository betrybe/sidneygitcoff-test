import importer.py
import xmltodict
import xml.etree.ElementTree as ET
from pathlib import Path

class XmlImporter(Importer):
    def __init__(self, arquivo)
    super.arquivo = arquivo

    def import_data():
        leituraArquivo = dict()

        if Path(caminho).suffix == '.xml':
            tree = ET.parse(caminho)
            leituraArquivo = xmltodict.parse(tree)
            return leituraArquivo
        else:
            return("Extensão do arquivo inválido")
