Tamanhos = ("PP", "P", "M", "G", "GG")

vitrine = [
    {"nome": "Camiseta Básica", "preço": 39.90, "tamanho": "M"},
    {"nome": "Calça Jeans", "preço": 129.90, "tamanho": "G"},
    {"nome": "Moletom", "preço": 159.90, "tamanho": "P"}
]

carrinho = [("Camiseta Básica", 3), ("Calça Jeans", 1)]

precos = {}
for produto in vitrine:
    precos[produto["nome"]] = produto["preço"]

total = 0
for nome, quantidade in carrinho:
    total = total + precos[nome] * quantidade

print("Peças na vitrine:", len(vitrine))
print("Total do carrinho : R$", round(total, 2))