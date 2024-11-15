media = int(input("Insira a média do aluno: "))

if media < 0:
    print(f"Olá Caique! >> MÉDIA INVÁLIDA. ABAIXO DO PERMITIDO <<")

elif media < 6:
    print(f"Olá Caique Sua média é: {media}, você esta de recuperação!")

elif  media >= 6:
    print(f"Olá, Caique! Sua média é: {media}, você tirou REGULAR!")

elif media == 10:
    print(f"Olá, Caique! Sua média é: {media}, voce tirou EXCELENTE!")

elif media < 10:
    print(f"Olá Caique! Sua média é:{media}, você tirou Bom!")