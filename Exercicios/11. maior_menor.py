#Autor: José Bezerra, Nov/2024    
#Leia três números e coloque em ordem crescente

MSG = "Digite um número:"
MSG_ORDEM = "Números em ordem crescente:"

try:
    a = int(input(MSG))
    b = int(input(MSG))
    c = int(input(MSG))

    if (a < b):
        if (c < a): #logo c < a < b
            print(MSG_ORDEM, c, a, b)
        else: 
            if (c < b):
                print(MSG_ORDEM, a, c, b)
            else:
                print(MSG_ORDEM, a, b, c)
    else: #Caso em que a > b
        if c < b:
            print(MSG_ORDEM, c, b, a)
        else:
            if (c < a):
                print(MSG_ORDEM, b, c, a)
            else:
                print(MSG_ORDEM, a, b, c)

except:
    print('Erro na conversão para int!')
    