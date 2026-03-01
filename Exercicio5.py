print("=== Verificador de Ano Bissexto ===")

ano = int(input("Digite o Ano Para Verificar Se Ele É Bissexto: "))

if (ano % 4 == 0 and  ano % 100 !=0) or (ano % 400 == 0 ):
    print(f"O Ano {ano} é Bissexto!!!")
    
else:
    print(f"O Ano {ano} Não é Bissexto!!!")
