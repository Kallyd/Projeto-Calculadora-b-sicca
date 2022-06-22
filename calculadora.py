#CALCULADORA COMPLEXA
selecao = int(input("Selecione 1 para conta de adição, 2 para conta de subtração e 3 para conta de divisão"))
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
    print(f"Resultado { div1 + div2 }")
else:
    print("Não foi possível efetuar a conta")