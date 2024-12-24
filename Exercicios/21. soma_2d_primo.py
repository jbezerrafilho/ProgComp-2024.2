numero = 2

while True: 
    primo = True

    #Este 'for' calcula se o número é primo
    for x in range(2, int(numero ** 0.5) + 1):
        # Com essa sintaxe na solução, não pode achar divisores
        if numero % x == 0:
            primo = False
            break  
         
    if primo:
        doisDigitos = numero
        # Fatiando o número até ficar com 02 dígitos
        while doisDigitos > 100:
            doisDigitos //= 10

        soma_digitos = doisDigitos // 10 + doisDigitos % 10       
        if soma_digitos == 10:
            print(f"O primo que somado seus dois primeiros algarismo resulta em {soma_digitos} é : {numero}.")
            break
    
    numero += 1