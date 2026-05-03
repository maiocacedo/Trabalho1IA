import heapq
import itertools

# Fila de prioridade usando heapq para garantir que o item com a menor prioridade seja sempre extraído primeiro.
class FilaPrioridade:
    def __init__(self):
        self.elementos = []
        self.contador = itertools.count() 
        
    def inserir(self, item, prioridade):
        id_unico = next(self.contador)
        heapq.heappush(self.elementos, (prioridade, id_unico, item))
        
    def extrair_minimo(self):
        if not self.esta_vazia():
            prioridade, id_unico, item = heapq.heappop(self.elementos)
            return item
        return None
        
    def esta_vazia(self):
        return len(self.elementos) == 0