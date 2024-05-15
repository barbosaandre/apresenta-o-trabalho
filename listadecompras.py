produtos = {
    'arroz': 9.00,
    'feijão': 12.00,
    'carne': 44.00,
    'pasta de dente': 3.50,
    'sabonete': 1.50,
    'shampoo': 6.75,
    'alface': 4.25
}

class ListaDeCompra:
    def _init_(self):
        self.itens = []
        self.valor_total = 0

lista = ListaDeCompra()

while True:
    produto = input("Qual produto você vai comprar? (Digite 'sair' para encerrar): ")
    produto = produto.lower()
    if produto == "sair":
        print("Bye!")
        break
    try:
        quant = int(input("Quantidade de produto: "))
        if quant <= 0:
            print("Por favor, insira uma quantidade válida maior que zero.")
            continue
    except ValueError:
        print("Por favor, insira um número válido para a quantidade.")
        continue
    
    if produto in produtos:
        total_produto = produtos[produto] * quant
        lista.valor_total += total_produto
        print(f"A lista de compras ficou com o seguinte valor: R${lista.valor_total:.2f}")
    else:
        print("Produto não encontrado.")
