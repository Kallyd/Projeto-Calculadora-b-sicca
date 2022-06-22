#CALCULADORA BÁSICA | BY KALLYD
print("Calculadora básica criada por Kallyd!!!")
print("Selecione as opções abaixo : ")
print("1 Para calculos de adição '+' ")
print("2 Para calculos de subtração '-' ")
print("3 Para calculos de divisão '/' ")
selecao = input("Digite a opção: ")
selecao = int(selecao)
#========================== [ ADIÇÃO ]  ===========================================
if selecao == 1 :
    print("Perfeito!! você selecionou a opção de adição, segue as regras abaixo!!")
    adicao1 = int(input("Digite o primeiro número: "))
    adicao2 = int(input("Digite o segundo número: "))
    print(f"Resultado: { adicao1 + adicao2 }")
# ===================== [ SUBTRAÇÃO ]  =====================================================================
elif selecao == 2 :
    print("Perfeito, você selecionou a opção de subtração, segue as regras abaixo!!")
    sub1 = int(input("Qual o primeiro número: "))
    sub2 = int(input("Qual o segundo número: "))
    print(f"Resultado { sub1 - sub2 }")
#============== [ DIVISÃO ] =====================================================================
elif selecao == 3:
    print("Perfeito!!, Você selecionou a opção de divisão!!")
    div1 = int(input("Qual o primeiro número: "))
    div2 = int(input("Qual o segundo número: "))
    print(f"Resultado { div1 // div2 }")
else:
    print("Você não selecionou a opção correta!!")
