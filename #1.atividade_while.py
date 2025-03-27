# LIMPEZA DE TERMINAL
import os
os.system("cls || clear")

sexo = input("Digite seu sexo : ")
idade = int(input("Digite sua idade : "))
salario = float(input("Digite seu sálario : "))
quantidade_de_salário = 0

while True:
    print("""
================ MENU ============
\tCódigo            Descrição
    1           |   Adicinar pessoa
    2           |   Exibir resultados
    3           |   Sair
    """)

    opcao = input("Digite o seu código : ")
    
    match opca:
        case 1:
            sexo = input("Digite seu sexo : ")
            idade = int(input("Digite sua idade : "))
            salario = float(input("Digite seu sálario : "))
        case 2:
            print(f"Sexo : {sexo}")
            print(f"Idade : {idade}")
            print(f"Salário : {salario}")
            media_salarial += salario / quantidade_de_salário
            idade_geral += idade
            if idade > idade_geral:
                print(f"Maior idade : {idade}")
            elif idade < idade_geral:
                print(f"Menor Sálario : {salario}")
            else:
                0
            if "Feminino":
                salario > 5.000
                print(f"Salário {salario}")
        case 3:
            break