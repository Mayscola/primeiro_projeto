texto = "Olá, meu nome é Caique"
partes = texto.split()
print(partes)

frase = "maçã,banana,laranja"
frutas = frase.split(",")
print(frutas)

dados = "nome:idade:cidade"
resultado = dados.split(":", maxsplit=1)
print(resultado)

texto = "olá, mundo"
maiusculo = texto.upper()
print(maiusculo)

nome_completo = "caique martins"
partes = nome_completo.split()  
primeiro_nome = partes[0].upper()  
print(primeiro_nome)