class Pilha:
    def __init__(self):
        self.itens = []
        
    def empilhar(self, item):
        self.itens.append(item)
        
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None
        
    def esta_vazia(self):
        return len(self.itens) == 0
        
    def tamanho(self):
        return len(self.itens)