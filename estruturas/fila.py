from collections import deque

# Fila simples usando deque para operações eficientes de enfileiramento e desenfileiramento.
class Fila:
    def __init__(self):
        self.itens = deque()
        
    def enfileirar(self, item):
        self.itens.append(item)
        
    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.popleft()
        return None
        
    def esta_vazia(self):
        return len(self.itens) == 0
        
    def tamanho(self):
        return len(self.itens)