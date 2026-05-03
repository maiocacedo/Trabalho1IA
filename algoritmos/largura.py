from estruturas.fila import Fila
from estruturas.operacoes_mapa import obter_vizinhos_validos
from visualizacao.animacao import animar_busca_tempo_real

# Função principal do algoritmo de Busca em Largura para encontrar o caminho mais curto do início ao destino, coletando recompensas no caminho.
def executar(mapa, inicio, destino, modo_visual=False):
    fila = Fila()
    fila.enfileirar((inicio, [inicio], 0))
    visitados = {inicio}
    nos_expandidos = 0
    recompensas_coletadas = []
    
    while not fila.esta_vazia():
        atual, caminho, custo_total = fila.desenfileirar()
        nos_expandidos += 1
        x, y = atual

        rec_pegas_ramo = [rec for rec in recompensas_coletadas if rec in caminho]

        if modo_visual:
            dados_visualizacao = {
                'g': custo_total,
                'recompensas': rec_pegas_ramo
            }
            animar_busca_tempo_real(mapa, atual, visitados, dados_estado=dados_visualizacao)
        
        
        if mapa[y][x] == '$' and atual not in recompensas_coletadas:
            recompensas_coletadas.append(atual)
            
        if atual == destino:
            return caminho, custo_total, nos_expandidos, recompensas_coletadas
            
        for vizinho, custo in obter_vizinhos_validos(mapa, x, y):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.enfileirar((vizinho, caminho + [vizinho], custo_total + custo))
                
    return None, 0, nos_expandidos, recompensas_coletadas