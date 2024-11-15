nome = "PAULA MARTINS"
mes = "JANEIRO"
valor_compra = 500.00
desconto = 10
cupom_de_desconto = nome.split()[0].upper() + "É10"  


mensagem = (f"Olá, {nome}. Em {mes} você realizou uma compra no valor de R${valor_compra} "  f"e ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom_de_desconto}.")
print(mensagem)
