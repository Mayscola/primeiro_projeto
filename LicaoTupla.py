lista = ['banana','maça','pera','banana']
tupla = (1,2,3,4)
meu_set = {1,2,3,4}
dicionario = {"nome": "Caique","idade": 22}



def add_fruta(a,b,c):
    lista.append(a)
    lista.append(b)
    lista.append(c)
    
    print(lista)

add_fruta("Limão","Morango","Uva")

for frutas in lista:
    print(f"Os elementos contidos na lista são: {frutas}")

var_txt = "Paralelepipedo"

for letras in var_txt:
    print(letras)

for x in lista:
    print (f"Os elementos contidos na lista são: {x}")

dicionario = {"nome": "Caique", "idade": 22}
for chave in dicionario:
    print (f"Aas chaves neste dicinário são: {chave}")

for w in dicionario.values():
    print (f"Os valores neste dicionário são: {w}")

dicionario = {"nome": "Caique", "idade": 22 }
for chave,valor in dicionario.items():
    print(dicionario["idade"])
    print(dicionario["nome"])
    print(f"Chave: {chave}, Valor: {valor}")
    