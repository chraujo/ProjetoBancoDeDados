import os
import base64
import json
from PIL import Image
from io import BytesIO

# Cria o diretório para salvar imagens, se ainda não existir
if not os.path.exists("imagens"):
    os.makedirs("imagens")

def salvar_imagem(blob, nome_arquivo):
    """
    Salva um blob de imagem em um arquivo no diretório 'imagens'.
    """
    caminho = os.path.join("imagens", nome_arquivo)
    try:
        with open(caminho, 'wb') as file:
            file.write(blob)
        print(f"Imagem salva em: {caminho}")
    except IOError as e:
        print(f"Erro ao salvar a imagem {nome_arquivo}: {e}")
    return caminho

def formatar_resultado(resultado):
    """
    Formata os resultados da consulta para exibição no terminal.
    - Salva blobs de imagem no diretório 'imagens' e retorna o caminho.
    - Decodifica bytes para texto se o campo não for uma imagem.
    - Converte dicionários para JSON formatado.
    """
    linhas_formatadas = []
    for linha in resultado:
        linha_formatada = []
        for campo in linha:
            if isinstance(campo, bytes):
                # Verifica se o campo é uma imagem
                try:
                    # Tenta abrir como imagem para confirmar se é uma imagem válida
                    with Image.open(BytesIO(campo)) as img:
                        nome_arquivo = f"imagem_{hash(campo)}.png"
                        caminho_imagem = salvar_imagem(campo, nome_arquivo)
                        campo = f"[Imagem salva em {caminho_imagem}]"
                except Exception:
                    # Caso não seja uma imagem, tenta decodificar como texto
                    try:
                        campo = campo.decode('utf-8', errors='ignore')
                    except UnicodeDecodeError:
                        campo = "[Dados binários não legíveis]"
            elif isinstance(campo, dict):
                # Converte dicionário para JSON formatado
                campo = json.dumps(campo, indent=2, ensure_ascii=False)
            linha_formatada.append(str(campo))
        linhas_formatadas.append(" | ".join(linha_formatada))
    return "\n".join(linhas_formatadas)
