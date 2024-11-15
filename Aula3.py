media = int(input("Insira a média do aluno: "))

if media < 0:
    print(f"Olá, Caique! >> MÉDIA INVÁLIDA. ABAIXO DO PERMITIDO <<")

elif media < 6:
    print(f"Olá, Caique! Sua média é: {media}, você está de recuperação!")

elif media == 10:
    print(f"Olá, Caique! Sua média é: {media}, você tirou EXCELENTE!")

elif media >= 6 and media < 10:
    print(f"Olá, Caique! Sua média é: {media}, você tirou BOM!")

else:
    print(f"Olá, Caique! Sua média é: {media}, você tirou REGULAR!")

