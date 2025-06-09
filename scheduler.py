import os
import zipfile
from datetime import datetime

def comprimir_xmls(diretorio="C:/Users/NicolasAvila/Desktop/Backup/BackupCTE_XML", destino="data"):
    arquivos = [f for f in os.listdir(diretorio) if f.endswith(".xml")]
    if not arquivos:
        return

    hoje = datetime.now().strftime("%Y-%m-%d")
    nome_zip = f"{destino}/{hoje}_cte.zip"

    with zipfile.ZipFile(nome_zip, "w") as zipf:
        for arquivo in arquivos:
            caminho = os.path.join(diretorio, arquivo)
            zipf.write(caminho, arcname=arquivo)

    print(f"✅ XMLs comprimidos: {nome_zip}")

    
