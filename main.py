import time
from mapas.leitor_mapa import carregar_mapa
from algoritmos import largura, profundidade, gulosa, a_estrela
from visualizacao.animacao import animar_rota, imprimir_mapa_estatico, salvar_print_arquivo, limpar_tela

# Função principal do sistema de navegação inteligente, com  menu e diversas opções.
def main():
    print("=== Sistema de Navegação Inteligente ===")
    mapa, agente, recompensas = carregar_mapa('mapa_teste.txt')
    
    if not mapa: return
        
    print(f"Mapa carregado. Dimensões: {len(mapa[0])}x{len(mapa)}")
    print(f"Posição do Agente (@): {agente}")
    print(f"Recompensas ($): {len(recompensas)}\n")
    saida_total = False
    while saida_total == False:
        limpar_tela()
        print("=== Sistema de Navegação Inteligente ===")
        print(f"Mapa carregado. Dimensões: {len(mapa[0])}x{len(mapa)}")
        print(f"Posição do Agente (@): {agente}")
        print(f"Recompensas ($): {len(recompensas)}\n")
        
        print("Digite 1 para continuar e 0 para encerrar o sistema.")
        escolha = input("Escolha: ")
        if escolha == '0':
            print("Encerrando o sistema..."); saida_total = True; time.sleep(3); break;

        print("\nDigite as coordenadas do destino (X Y) ou -1 -1 para encerrar:")
        
        try:
            dest_x = int(input("Digite a coordenada de destino X: "))
            dest_y = int(input("Digite a coordenada de destino Y: "))
            
            if dest_x == -1 and dest_y == -1:
                print("Encerrando o sistema..."); saida_total = True; time.sleep(3); break; 
            
            destino = (dest_x, dest_y)
        except ValueError:
            print("Entrada inválida. Digite números inteiros."); time.sleep(3); continue; 

        if destino[0] >= len(mapa[0]) or destino[1] >= len(mapa) or destino[0] < 0 or destino[1] < 0:
            print(f"Coordenadas fora dos limites do mapa, digite dentro dos limites ({len(mapa[0]) - 1}x{len(mapa) - 1}).");time.sleep(3); continue; 
        if mapa[destino[1]][destino[0]] == '▓':
            print("O destino é uma parede. Encerrando a Busca...\n\n");time.sleep(3); continue; 

        print("\nComo deseja executar?")
        print("1 - Modo Comparativo (Executar todos os algoritmos e comparar resultados)")
        print("2 - Modo Detalhado (Ver o algoritmo explorando em tempo real)")
        modo_exec = input("Escolha (1 ou 2): ")

        if modo_exec == '2':
            print("\nQual algoritmo deseja analisar?")
            print("1 - Largura (BFS)\n2 - Profundidade (DFS)\n3 - Gulosa\n4 - A*")
            escolha = input("Escolha: ")
            
            if escolha == '1': largura.executar(mapa, agente, destino, modo_visual=True)
            elif escolha == '2': profundidade.executar(mapa, agente, destino, modo_visual=True)
            elif escolha == '3': gulosa.executar(mapa, agente, destino, recompensas, modo_visual=True)
            elif escolha == '4': a_estrela.executar(mapa, agente, destino, recompensas, modo_visual=True)
            

        print("\nCalculando rotas....\n")
        resultados = {}

        t0 = time.perf_counter()
        resultados['1'] = largura.executar(mapa, agente, destino) + (time.perf_counter() - t0,)

        t0 = time.perf_counter()
        resultados['2'] = profundidade.executar(mapa, agente, destino) + (time.perf_counter() - t0,)

        t0 = time.perf_counter()
        resultados['3'] = gulosa.executar(mapa, agente, destino, recompensas) + (time.perf_counter() - t0,)

        t0 = time.perf_counter()
        resultados['4'] = a_estrela.executar(mapa, agente, destino, recompensas) + (time.perf_counter() - t0,)

        
        print("=== COMPARATIVO DE PERFORMANCE ===")
        
        
        for nome, dados in resultados.items():
            caminho, custo, expandidos, rec_pegas, tempo = dados
            status = "Alcançado" if caminho else "Sem Solução"
            
            if nome == '1': nome = "BFS(Largura)"
            elif nome == '2': nome = "DFS(Profundidade)"
            elif nome == '3': nome = "Gulosa"
            elif nome == '4': nome = "A*"
            
            print(f"[{nome}]\tStatus: {status} | Custo: {custo} | Passos: {len(caminho) if caminho else 0}")
            print(f"\tExpandidos: {expandidos} | Tempo: {tempo:.6f}s | Rec. Pegas: {len(rec_pegas)} \n -- \n")
        time.sleep(7)
        saida = False
        while saida == False:
            time.sleep(3)
            limpar_tela()
            
            print("\nO que deseja fazer com as rotas encontradas?")
            print("1 - Animar rota final do agente")
            print("2 - Mostrar Último Estado no terminal")
            print("3 - Salvar Estado final em arquivo .txt")
            print("0 - Sair para o menu principal")
            
            opcao_pos = input("\nEscolha: ")
            if opcao_pos == '0': print("Retornando ao menu principal..."); saida = True; continue;
            if opcao_pos in ['1', '2', '3']:
                escolha = input("Qual algoritmo? (BFS - Largura(1) | DFS - Profundidade(2) | Gulosa(3) | A* - Estrela(4)): ")
                if escolha in resultados:
                    escolha_caminho = resultados[escolha][0]
                    recompensas_esc = resultados[escolha][3]
                    
                    if opcao_pos == '1': animar_rota(mapa, escolha_caminho, recompensas_esc, destino)
                    elif opcao_pos == '2': imprimir_mapa_estatico(mapa, escolha_caminho, f"Rota Final - {escolha}")
                    elif opcao_pos == '3': salvar_print_arquivo(mapa, escolha_caminho, f"rota_{escolha}.txt")
                    
                else:
                    print("Algoritmo não encontrado.")
    return

if __name__ == "__main__":
    main()