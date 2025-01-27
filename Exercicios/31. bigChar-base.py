bigchars = [
"               AAA               ",
"              A:::A              ",
"             A:::::A             ",
"            A:::::::A            ",
"           A:::::::::A           ",
"          A:::::A:::::A          ",
"         A:::::A A:::::A         ",
"        A:::::A   A:::::A        ", 
"       A:::::A     A:::::A       ",  
"      A:::::AAAAAAAAA:::::A      ",
"     A:::::::::::::::::::::A     ",
"    A:::::AAAAAAAAAAAAA:::::A    ", 
"   A:::::A             A:::::A   ",  
"  A:::::A               A:::::A  ",
" A:::::A                 A:::::A ",
"AAAAAAA                   AAAAAAA",

]

# Esse 'menor_inicio e maior_fim' irão delimitar o retângulo
# necessário para imprimir corretamente o caractere
menor_inicio = 10000
maior_fim = -1
for linha in bigchars:
    inicio = linha.find('A')
    fim = linha.rfind('A')
    menor_inicio = min(menor_inicio, inicio)
    maior_fim = max(maior_fim, fim)
   
    
for linha in bigchars:
    # Imprimi o trecho necessário para desenhar o A
    print(linha[inicio:fim+1])
