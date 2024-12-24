print("Qual o capital que irá render à juros compostos?")
capital = float(input())

print("Qual o valor da taxa de juros?")
taxa = float(input())

print("Qual o tempo de aplicação?")
tempo = int(input())

montante = capital * (1 + (taxa / 100)) ** tempo
montante = round(montante, 2)
print(" O valor de R$ ", capital, " aplicado à taxa de ", 
       taxa, "  +   renderá o montante de R$ ", montante)
