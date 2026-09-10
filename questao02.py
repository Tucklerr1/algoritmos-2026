from funcoes import delimitador_intervalo
vet=[14,2,63,27,3,49,52,10,77,1]
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
intervalo = delimitador_intervalo(n1,n2,vet)
print(f"A soma dos elementos no intervalo de {n1} até {n2} é {intervalo}")