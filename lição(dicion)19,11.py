dicionario1 = {"nome": "Carlos", "idade": "35", "profissão": "Gari"}
dicionario2 = {"nome": "Miguel", "idade": "37", "profissão": "Jogador"}

dicionarios = [
    {"nome": "Miguel", "idade": "35"},
    {"nome": "Marcos", "idade": "27"}
]
dados = []


for dicionario in dicionarios:

    dados.append(f"{dicionario['nome']}")
print(f"O valor contido na chave 'nome' é: {dicionario['nome']} ({dicionario['idade']} anos)")

#Anexar os dados contidos 
print(f"Os dados anexados são:{','.join(dados)}")