clientes = [
  {"nome": "PAULA MARTINS", "mes": "JANEIRO", "valor": 500.00}
]

desconto = 10

for cliente in clientes:
    nome = cliente["nome"]
    mes = cliente ["mes"]
    valor = cliente["valor"]
    cupom = nome.split()[0].upper() + "É10"

    mensagem = (
        f" Olá, {nome}. Em {mes} voce realizou uma compra no valor de R${valor:.2f}"
        f" .\nE ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom}."
    )

    print(mensagem)