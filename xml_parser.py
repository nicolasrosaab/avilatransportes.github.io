import os
import xml.etree.ElementTree as ET

def extrair_dados_xml(pasta_xml="C:/Users/NicolasAvila/Desktop/Backup/BackupCTE_XML"):
    resultados = []
    for nome_arquivo in os.listdir(pasta_xml):
        if nome_arquivo.endswith(".xml"):
            caminho = os.path.join(pasta_xml, nome_arquivo)
            try:
                tree = ET.parse(caminho)
                root = tree.getroot()
                emit = root.find(".//emit")
                dest = root.find(".//dest")
                total = root.find(".//vNF")
                
                resultados.append({
                    "arquivo": nome_arquivo,
                    "emitente": emit.find("xNome").text if emit is not None else "Desconhecido",
                    "destinatario": dest.find("xNome").text if dest is not None else "Desconhecido",
                    "valor": float(total.text) if total is not None else 0.0,
                })
            except Exception as e:
                resultados.append({"arquivo": nome_arquivo, "erro": str(e)})
    return resultados
