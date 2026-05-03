CUSTOS_TERRENO = {' ': 1, 'A': 4, 'R': 10, 'P': 20}

# Função para obter os vizinhos válidos de uma posição no mapa, considerando os custos de terreno e obstáculos.
def obter_vizinhos_validos(mapa, x, y):
    vizinhos = []
    for distancia_x, distancia_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x + distancia_x, y + distancia_y
        if 0 <= nx < len(mapa[0]) and 0 <= ny < len(mapa):
            terreno = mapa[ny][nx]
            if terreno != '▓':
                custo = CUSTOS_TERRENO.get(terreno, 1)
                vizinhos.append(((nx, ny), custo))
    return vizinhos