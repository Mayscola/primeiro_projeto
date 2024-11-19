Minha_tupla = (1,2,3,4,5,8,'banana')
Minha_lista = list( Minha_tupla)

Minha_lista.extend([6,7,8])

Minha_lista.pop(0)
Minha_lista.pop()

print(f"Imprima o primeiro dado da lista : {Minha_lista[0]}")
print(f"Imprima todos os dados da lista: {len(Minha_lista)}")
print(f"Imprima todos os dados da lista: {Minha_lista}")


