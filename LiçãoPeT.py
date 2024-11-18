nome_PET = input("Insira o nome do PET: ")
idade_humana_do_pet = int(input(f"Insira a idade humana do PET: "))
conversao_da_idade = idade_humana_do_pet * 7
print(f"A idade do {nome_PET} em anos de PET é: {conversao_da_idade}")

porte_pet = input("Qual seria o porte do seu PET? (Pequeno, Medio, Grande e Gigante): ")
quantos_meses= int(input("Quantos meses o Pet, irá tomar banho ? "))

if porte_pet == 'Pequeno':
    banho = 50.00
    custo = 5.00
elif porte_pet == 'Medio':
    banho = 60.00
    custo = 15.00
elif porte_pet == 'Grande':
    banho = 75.00
    custo = 20.00
elif porte_pet == 'Gigante':
    banho = 80.00
    custo = 20.00    
else:
    print("Porte inválido! Por favor, insira pequeno, medio ou grande.")
   


if banho > 0:  
    lucro_por_banho = banho - custo
    lucro_total = lucro_por_banho  * quantos_meses
    print(f"Olá {nome_PET}, tem {conversao_da_idade} anos e nos últimos {quantos_meses} meses, o lucro com este pet foi de R${lucro_total}")

    
else:
    print("Nenhum cálculo foi realizado devido a erro no porte do PET.")