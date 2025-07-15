import sys
from queries import (
    consulta_midia_por_tipo,
    consulta_distribuicao_geografica,
    consulta_midia_com_imagens,
    consulta_plataformas_por_midia,
    consulta_motivos_por_midia,
    consulta_agentes_alvos,
    consulta_midia_por_pais_e_tipo
)
from utils import formatar_resultado

def mostrar_menu():
    print("Aplicação CLI - Consultas de Banco de Dados")
    print("Escolha uma opção:")
    print("1. Ver mídias por tipo")
    print("2. Ver distribuição geográfica das mídias")
    print("3. Ver mídias com imagens")
    print("4. Ver mídias por plataforma")
    print("5. Ver motivos por mídia")
    print("6. Ver interações entre agentes e alvos")
    print("7. Contagem de mídias por país e tipo")
    print("8. Sair")

def executar_opcao(opcao):
    if opcao == "1":
        tipo = input("Digite o tipo de mídia (ex.: 'vídeo, imagem, áudio'): ")
        resultado = consulta_midia_por_tipo(tipo)
        print(f"Resultado da Consulta - Mídias do Tipo '{tipo}':")
        print(formatar_resultado(resultado))
    elif opcao == "2":
        resultado = consulta_distribuicao_geografica()
        print("Resultado da Consulta - Distribuição Geográfica das Mídias:")
        print(formatar_resultado(resultado))
    elif opcao == "3":
        resultado = consulta_midia_com_imagens()
        print("Resultado da Consulta - Mídias com Imagens:")
        print(formatar_resultado(resultado))
    elif opcao == "4":
        resultado = consulta_plataformas_por_midia()
        print("Resultado da Consulta - Mídias por Plataforma:")
        print(formatar_resultado(resultado))
    elif opcao == "5":
        resultado = consulta_motivos_por_midia()
        print("Resultado da Consulta - Motivos por Mídia:")
        print(formatar_resultado(resultado))
    elif opcao == "6":
        resultado = consulta_agentes_alvos()
        print("Resultado da Consulta - Interações entre Agentes e Alvos:")
        print(formatar_resultado(resultado))
    elif opcao == "7":
        resultado = consulta_midia_por_pais_e_tipo()
        print("Resultado da Consulta - Contagem de Mídias por País e Tipo:")
        print(formatar_resultado(resultado))
    elif opcao == "8":
        print("Saindo...")
        sys.exit()
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ")
        executar_opcao(opcao)

if __name__ == "__main__":
    main()
