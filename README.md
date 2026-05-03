# Trabalho de IA - Sistema de Navegação Inteligente

O objetivo desse trabalho é demonstrar os algoritmos de busca na prática. O agente deve encontrar o melhor caminho em um mapa .txt com recompensas, terrenos diferentes e paredes.
Para isso, foi implementado Busca em Largura, Profundidade, Gulosa e A*.

# Arquitetura

## Algoritmos
Onde estão localizados os algoritmos de busca:
- largura.py
- profundidade.py
- gulosa.py
- a_estrela.py

## Estruturas
Onde estão as estruturas de dados e a função heurística (aplicadas em Busca Gulosa e A*) necessárias para a criação dos algoritmos. Além disso, temos as operações realizadas no mapa:
- fila.py
- fila_prioridade.py
- heuristica.py
- operacoes_mapa.py
- pilha.py

## Mapas
Onde estão os mapas e o leitor de mapas:
- leitor_mapa.py
- mapa_teste.txt

## Visualização
Onde estão as animações do mapa e a rota realizada pelo agente 
- animacao.py

# Função Heurística adotada

A função é dinâmica e ajusta a estimativa com base na proximidade de recompensas disponíveis.
$$h(n) = \max(0, D(n, destino)-B(n, recompensas))$$
onde,
$$D(n, destino)=|x_{n}-x_{destino}|+|y_{n}-y_{destino}|$$
$$B(n, recompensas)=\frac{15}{d_{prox}+1}$$

D representa a distância entre o agente e o destino.
B utilizada para que o agente analise a recompensa mais próxima. O número 15 representa uma constante de calibração, age como um peso. Valor escolhido com base nos custos, para que aja equilibrio.

