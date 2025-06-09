from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from xml_parser import extrair_dados_xml
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dashboard")
def dados_dashboard():
    caminho = "data/2024-06"
    dados = extrair_dados_xml(caminho)
    return {"registros": dados}
