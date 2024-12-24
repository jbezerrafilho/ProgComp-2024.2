#Autor: José Bezerra
#Sugestão de testes para coeficiente a, b e c;
#a = 1, b = -5, c = 6; 
#a = 2, b = 4, c = 2;
#a = 1, b = 2, c = 5

a = int(input("Digite o coeficiente a para a equação de 2º grau: "))

if a != 0:
    b = int(input("Digite o coeficiente b para a equacao de 2º grau: "))
    c = int(input("Digite o coeficiente c para a equacao de 2º grau: "))
    delta = b ** 2 - 4*a*c
    if delta < 0:
        print("Equação sem raízes reais, pois o Delta é menor que 0!")
    else:
        x1 = (- b + delta ** (1/2)) / ( 2 * a )
        x2 = (- b - delta ** (1/2)) / ( 2 * a )
        if x1 == x2:
            print(f'Equação possui raiz única na valor de {x1}, devido o Delta ser 0.')
        else:
            print("O valor de x1 é:", x1)
            print("O valor de x2 é:", x2)
else:
    print("O coeficiente 'a' não pode ser 0!")
