from estruturas.fila_prioridade import FilaPrioridade
from estruturas.operacoes_mapa import obter_vizinhos_validos
from estruturas.heuristica import heuristica_dinamica
from visualizacao.animacao import animar_busca_tempo_real

# Função principal do algoritmo Guloso para encontrar o caminho mais curto do início ao destino, considerando as recompensas restantes.
def executar(mapa, inicio, destino, todas_recompensas, modo_visual=False):
    fila = FilaPrioridade()
    recompensas_iniciais = tuple(todas_recompensas)
    
    h_ini = heuristica_dinamica(inicio, destino, recompensas_iniciais)
    fila.inserir((inicio, [inicio], 0, recompensas_iniciais), h_ini)
    
    visitados = set()
    nos_expandidos = 0
    visitados_coords = set()
    
    while not fila.esta_vazia():
        atual, caminho, custo_real_acumulado, recompensas_restantes = fila.extrair_minimo()
        nos_expandidos += 1
        
        est_visitado = (atual, recompensas_restantes)
        if est_visitado in visitados: 
            continue
            
        visitados.add(est_visitado)
        visitados_coords.add(atual)
        
        if modo_visual:
             h_atual_display = heuristica_dinamica(atual, destino, recompensas_restantes)
             rec_pegas_ramo = [r for r in todas_recompensas if r not in recompensas_restantes]
             
             dados_visualizacao = {
                'g': custo_real_acumulado, 
                'h': h_atual_display,
                'f': h_atual_display, 
                'recompensas': rec_pegas_ramo
             }
             animar_busca_tempo_real(mapa, atual, visitados_coords, dados_estado=dados_visualizacao)
        
        if atual == destino:
            rec_pegas = [r for r in todas_recompensas if r not in recompensas_restantes]
            return caminho, custo_real_acumulado, nos_expandidos, rec_pegas
            
        for viz, custo_mov in obter_vizinhos_validos(mapa, atual[0], atual[1]):
            novo_custo_real = custo_real_acumulado + custo_mov
            
            novas_recompensas = list(recompensas_restantes)
            if viz in novas_recompensas: 
                novas_recompensas.remove(viz)
            novas_recompensas_tuple = tuple(novas_recompensas)
            
            h_viz = heuristica_dinamica(viz, destino, novas_recompensas_tuple)
            fila.inserir((viz, caminho + [viz], novo_custo_real, novas_recompensas_tuple), h_viz)
                                 
    return None, 0, nos_expandidos, []