import pytest

from Loja.carrinho import (
    Carrinho,
    CarrinhoFinalizadoError,
)
from Loja.produto import Produto


def carrinho_exemplo():
    c = Carrinho()

    c.adicionar(
        Produto("Camiseta básica", 39.90, "M"),
        3
    )

    c.adicionar(
        Produto("Calça jeans", 129.90, "G")
    )

    return c


def test_subtotal_e_quantidade():
    c = carrinho_exemplo()

    assert c.quantidade_de_pecas == 4
    assert c.subtotal == pytest.approx(249.60)


def test_acima_de_200_frete_gratis():
    assert carrinho_exemplo().total == pytest.approx(249.60)


def test_abaixo_de_200_paga_frete():
    c = Carrinho()

    c.adicionar(
        Produto("Boné", 35, "M")
    )

    assert c.total == pytest.approx(50.0)


def test_recusa_quem_nao_e_produto():
    with pytest.raises(TypeError):
        Carrinho().adicionar(
            ("Boné", 35),
            1
        )


def test_quantidade_deve_ser_positiva():
    c = Carrinho()

    produto = Produto(
        "Boné",
        35,
        "M"
    )

    with pytest.raises(ValueError):
        c.adicionar(produto, 0)

    with pytest.raises(ValueError):
        c.adicionar(produto, -1)


def test_finalizar_e_impede_novas_pecas():
    with pytest.raises(ValueError):
        Carrinho().finalizar()

    c = Carrinho()

    c.adicionar(
        Produto("Boné", 35, "M")
    )

    c.finalizar()

    with pytest.raises(CarrinhoFinalizadoError):
        c.adicionar(
            Produto("Camiseta", 39.90, "M")
        )


def test_itens_devolve_uma_copia():
    c = Carrinho()

    c.adicionar(
        Produto("Boné", 35, "M")
    )

    itens = c.itens
    itens.clear()

    assert c.quantidade_de_pecas == 1