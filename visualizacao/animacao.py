import os
import time

from estruturas.operacoes_mapa import CUSTOS_TERRENO

# Funções para animar a busca e a rota final no terminal, com visualização em tempo real do processo de exploração e do caminho encontrado.

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animar_busca_tempo_real(mapa_matriz, atual, visitados, delay=0.3, dados_estado=None):
    limpar_tela()
    mapa_print = [linha[:] for linha in mapa_matriz]
    
    for vx, vy in visitados:
        if mapa_print[vy][vx] not in ['▓', '@', '$', 'A', 'R', 'P']:
            mapa_print[vy][vx] = '~'
            
    ax, ay = atual[0], atual[1]

    if mapa_print[ay][ax] not in ['@', '$', 'A', 'R', 'P', '▓']:
        mapa_print[ay][ax] = 'O'
        
    print("=== Explorando o Mapa ===")
    for linha in mapa_print: 
        print("".join(linha))
        
    print(f"\n--- Analisando nó: {atual} ---")
    print(f"Nós na memória (visitados): {len(visitados)}")
    
    if dados_estado:
        custo_g = dados_estado.get('g', 'N/A')
        heuristica_h = dados_estado.get('h', 'N/A')
        custo_f = dados_estado.get('f', 'N/A')
        rec_coletadas = dados_estado.get('recompensas', [])
        
        print(f"Custo Real Acumulado g(n): {custo_g}")
        if heuristica_h != 'N/A':
             print(f"Valor da Heurística  h(n): {heuristica_h:.2f}")
             print(f"Custo Total          f(n): {custo_f:.2f}")
        
        print(f"Recompensas no Ramo Atual: {len(rec_coletadas)} coletadas")
        if rec_coletadas:
            print(f"Coordenadas das Recompensas: {rec_coletadas}")

    time.sleep(delay)
        

    

def animar_rota(mapa_matriz, caminho, recompensas_coletadas, destino_final):
    if not caminho: 
        return print("Nenhum caminho encontrado!")
        
    mapa_animacao = [linha[:] for linha in mapa_matriz]
    inicio_x, inicio_y = caminho[0]
    
    if mapa_animacao[inicio_y][inicio_x] == '@': 
        mapa_animacao[inicio_y][inicio_x] = '.'

    custo_acumulado = 0
    recompensas_pegas_ate_agora = 0

    for passo, (x, y) in enumerate(caminho):
        limpar_tela()
        pos_anterior = mapa_animacao[y][x]
        
        if passo > 0:
            terreno = mapa_matriz[y][x]
            if terreno != 'X':
                custo_passo = CUSTOS_TERRENO.get(terreno, 1)
                custo_acumulado += custo_passo

        if pos_anterior == '$': recompensas_pegas_ate_agora += 1
            
        if pos_anterior == ' ': pos_anterior = '~' 
             
        mapa_animacao[y][x] = '@' 
        
        print(f"=== Movimentação do Agente ===")
        for linha in mapa_animacao: 
            print("".join(linha))
            
        print(f"\n=== Status do Passo {passo + 1} de {len(caminho)} ===")
        if passo > 0:
            print(f"Terreno pisado: '{terreno}' (+{custo_passo} de custo)")
        print(f"Custo Total Acumulado: {custo_acumulado}")
        print(f"Recompensas Coletadas: {recompensas_pegas_ate_agora} de {len(recompensas_coletadas)}")
        
        if (x, y) == destino_final:
            print("\n=== DESTINO FINAL ALCANÇADO! ===")
            print(f"Custo Final da Rota: {custo_acumulado}")
            print(f"Total de Recompensas: {recompensas_pegas_ate_agora}")
        
        time.sleep(0.5)
        
        mapa_animacao[y][x] = '.' if pos_anterior == '$' else pos_anterior
        
def imprimir_mapa_estatico(mapa_matriz, caminho, titulo="Estado do Mapa"):
    if not caminho: return print(f"\n{titulo}\nNenhum caminho encontrado.")
    
    mapa_print = [linha[:] for linha in mapa_matriz]
    for x, y in caminho:
        if mapa_print[y][x] not in ['@', '$']: mapa_print[y][x] = '*'
            
    fim_x, fim_y = caminho[-1]
    mapa_print[fim_y][fim_x] = '@'

    print(f"\n--- {titulo} ---")
    for linha in mapa_print: print("".join(linha))
    print("--- Fim do Mapa ---\n")
    time.sleep(7)

def salvar_print_arquivo(mapa_matriz, caminho, nome_arquivo="resultado_rota.txt"):
    if not caminho: return
    
    mapa_print = [linha[:] for linha in mapa_matriz]
    for x, y in caminho:
        if mapa_print[y][x] not in ['@', '$']: mapa_print[y][x] = '~'
            
    fim_x, fim_y = caminho[-1]
    mapa_print[fim_y][fim_x] = '@'

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(f"Caminho Total: {len(caminho)} passos\n\n")
            for linha in mapa_print: f.write("".join(linha) + "\n")
        print(f"\n Print do mapa salvo com sucesso no arquivo '{nome_arquivo}'!")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")