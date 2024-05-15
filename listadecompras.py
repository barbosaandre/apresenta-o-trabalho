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
    def __init__(self):
        self.itens = {}
        self.valor_total = 0

    def adicionar_item(self, produto, quantidade):
        if produto in produtos:
            if produto in self.itens:
                self.itens[produto] += quantidade
            else:
                self.itens[produto] = quantidade

            total_produto = produtos[produto] * quantidade
            self.valor_total += total_produto
            print(f"{quantidade}x {produto} adicionado à lista.")
            print(f"A lista de compras ficou com o seguinte valor: R${self.valor_total:.2f}")
        else:
            print("Produto não encontrado.")

    def mostrar_itens(self):
        print("Itens na lista de compras:")
        for produto, quantidade in self.itens.items():
            print(f"{quantidade}x {produto}")

lista = ListaDeCompra()

while True:
    comando = input("Você quer (1) adicionar um item ou (2) mostrar a lista de compras? (Digite 'sair' para encerrar): ")
    if comando.lower() == "sair":
        lista.mostrar_itens()
        print("Bye!")
        break
    elif comando == "1":
        produto = input("Qual produto você vai comprar? (Digite 'sair' para encerrar): ")
        produto = produto.lower()
        if produto == "sair":
            continue
        try:
            quant = int(input("Quantidade de produto: "))
            if quant <= 0:
                print("Por favor, insira uma quantidade válida maior que zero.")
                continue
        except ValueError:
            print("Por favor, insira um número válido para a quantidade.")
            continue

        lista.adicionar_item(produto, quant)
    elif comando == "2":
        lista.mostrar_itens()
    else:
        print("Comando inválido. Por favor, escolha '1', '2' ou 'sair'.")
