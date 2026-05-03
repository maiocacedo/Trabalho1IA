# Heurística dinâmica que ajusta a estimativa com base na proximidade de recompensas disponíveis.
def heuristica_dinamica(atual, destino, recompensas_disponiveis):
    distancia_objetivo = abs(atual[0] - destino[0]) + abs(atual[1] - destino[1])
    bonus_atracao = 0
    
    if recompensas_disponiveis:
        distancias_recompensas = [abs(atual[0] - r[0]) + abs(atual[1] - r[1]) for r in recompensas_disponiveis]
        dist_prox = min(distancias_recompensas)
        if dist_prox <= 6:
            bonus_atracao = 15 / (dist_prox + 1)
            
    return max(0, distancia_objetivo - bonus_atracao)