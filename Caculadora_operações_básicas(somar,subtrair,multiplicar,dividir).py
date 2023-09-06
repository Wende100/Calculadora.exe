print("""
=========================================== BEM-VINDO-A-CAULCULADORA ===========================================
""")

nome = input("seu nome e : ")

print(f"se já bem vindo {nome.upper()} a sua Calculadora!")

      
numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))


while True:
  
    
 opcao = int(input(f"selecione a opção\n[1]somar:\n[2]subtrair:\n[3]multiplicar:\n[4]dividir:\n[5]sair!"))

 if opcao == 1:
  print(f"resulta da soma e {numero1+numero2}")

 elif opcao == 2:
  print(f"o resultado e {numero1-numero2}")
    
 elif opcao == 3:
  print(f"o resultado e {numero1*numero2}")
 elif opcao == 4:
  print(f"o resultado e {numero1/numero2}")
    
 elif opcao == 5:
  print(f"saindo!...")   
  break
 else:
  print("opção invalida!")
 