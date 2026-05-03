import os

# Função para carregar o mapa a partir de um arquivo de texto, identificando a posição do agente e das recompensas.
def carregar_mapa(nome_arquivo):
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(caminho_base, nome_arquivo)
    
    mapa_matriz = []
    posicao_agente = None
    posicoes_recompensas = []

    try:
        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            for y, linha in enumerate(arquivo.readlines()):
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                
                linha_mapa = []
                for x, char in enumerate(linha_limpa):
                    linha_mapa.append(char)
                    if char == '@':
                        posicao_agente = (x, y)
                    elif char == '$':
                        posicoes_recompensas.append((x, y))
                mapa_matriz.append(linha_mapa)
                
        return mapa_matriz, posicao_agente, posicoes_recompensas
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado na pasta 'mapas'.")
        return None, None, None