import datetime

class SimpleReport:

    def __init__(self):

# metodo estatico que nao necessita de instancia para ser utilizado
    @staticmethod 
    def generate(dictionary):
        dataFabricacaoAntiga
        dataValidadeMaisProxima
        nomeEmpresa = ""
        listaDeEmpresas = []
        qtdEstoque = 0
        for v in dictionary:
            if v["data_de_fabricacao"] < dataFabricacaoAntiga:
                dataFabricacaoAntiga = v["data_de_fabricacao"]

            if v["data_de_validade"] < dataValidadeMaisProxima:
                dataValidadeMaisProxima = v["data_de_validade"]
            
        listaDeEmpresas = dictionary.keys()
        
        i=0
        listaDeEmpresasContagem = []
        nomeEmpresaAnterior = ""
        for value in listaDeEmpresas:
            if i == 0:
                listaDeEmpresasContagem.append(value, listaDeEmpresas.count(value))
                nomeEmpresaAnterior = value
                i+=1
            else:
                if value != nomeEmpresaAnterior:
                    listaDeEmpresasContagem.append({"nome_empresa": value, "qtdEstoque": listaDeEmpresas.count(value)})
                    nomeEmpresaAnterior = value
                    i+=1
        

        listaDeEmpresasContagem.sort(reverse = true, key="qtdEstoque")
        
        return ("Data de Fabricação mais antiga: ", dataFabricacaoAntiga,
        "\nData de validade mais próxima: ", dataValidadeMaisProxima , 
        "\nEmpresa com maior quantidade de produtos estocados: " list(listaDeEmpresasContagem())[0], )