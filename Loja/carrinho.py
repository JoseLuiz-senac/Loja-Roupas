class Carrinho:
    def __init__(self):
        self._itens = [] # pares (produto, quantidade)
        self._finalizado = False

    def adicionar(self, produto, quantidade=1):
        if self._finalizado:
            raise CarrinhoFinalizadoError("carrinho finalizado não recebe peças")
        if not isinstance(produto, Produto):
            raise TypeError("só é possível adicionar um Produto")
        if quantidade <= 0:
            raise ValueError("quantidade deve ser positiva")
        self._itens.append((produto, quantidade))


@property
def itens(self):
    return list(self._itens) # uma cópia
@property
def quantidade_de_pecas(self):
    return sum(quantidade for _, quantidade in self._itens)
@property
def subtotal(self):
    return total_carrinho([(p.preco, q) for p, q in self._itens])
@property
def total(self):
    return self.subtotal + frete(self.subtotal)
def finalizar(self):
    if not self._itens:
        raise ValueError("não é possível finalizar um carrinho vazio")
    self._finalizado = True

def carrinho_exemplo():
    c = Carrinho()
    c.adicionar(Produto("Camiseta básica", 39.90, "M"), 3)
    c.adicionar(Produto("Calça jeans", 129.90, "G"))
    return c

def test_subtotal_e_quantidade():
    c = carrinho_exemplo()
    assert c.quantidade_de_pecas == 4
    assert c.subtotal == pytest.approx(249.60)
def test_acima_de_200_frete_gratis():
    assert carrinho_exemplo().total == pytest.approx(249.60)