dados = '''0718730-0;AABAN VASCONCELOS ZYZZYAG;3;3;1,5;10
0763186-3;ABDIAS NICACIO SANTOS SILVA PIRES BELFORT;3;3;3;10
0737811-4;ABDRAMAR PEREIRA SOUSA NASCIMENTO;6;3;5,25;21,25
0814834-1;ABEL BIZERRA DA SILVA NETO;2,25;2,25;3;10
0749150-6;ABEL CARLOS BASILIO;2,25;3,75;2,25;10
0758834-8;ABEL DE CARVALHO SIQUEIRA NETO;5,25;3;3,75;22,5
0800099-9;ABEL RICARDO DE SOUZA ALVES;4,5;3,75;2,25;7,5
0705043-7;ABEL RICARDO JORGE DA SILVA;0,75;1,5;3;16,25'''

candidatos = dados.replace(",", ".").split("\n")


dados_tratados = []
for candidato in candidatos:
    candidato = candidato.split(";")
    
    for pos in range(2, 6):
        candidato[pos] = float(candidato[pos])

    candidato.append(sum(candidato[2:6]))
    dados_tratados.append(candidato)
    

for candidato in dados_tratados:
    print(candidato)

aprovados = filter(lambda x: x[2] >= 2 and x[3] >= 2 and x[4] >= 2 and x[5] >= 2 and x[6] >= 10, dados_tratados)
for aprovado in aprovados:
    print(aprovado[1], aprovado[6])