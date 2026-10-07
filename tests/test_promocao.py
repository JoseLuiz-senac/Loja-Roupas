import pytest

from Loja.carrinho import Carrinho
from Loja.produto import Produto
from Loja.promocao import SemPromocao, Percentual, Cupom

def carrinho_com(promocao):
    c = Carrinho(promocao)
    c.adicionar(Produto("Camiseta básica", 39.90, "M"), 3)
    c.adicionar(Produto("Calça jeans", 129.90, "G"))
    return c 


@pytest.mark.parametrize("promocao, esperado", [
    (SemPromocao(), 249.60),
    (Percentual(10), 224.64), 
    (Cupom(100), 164.60), 
])
def test_total_com_cada_promocao(promocao, esperado):
    assert carrinho_com(promocao).total == pytest.approx(esperado)
