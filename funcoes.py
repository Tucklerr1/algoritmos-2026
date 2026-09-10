def verificador(num, vet):
    for i in range(0,9):
        if num == vet[i]:
            return f'O número existe dentro do vetor e está na posição {i}.'
    return f'O número não existe dentro do vetor.'

def delimitador_intervalo(n1, n2, vet):
    soma = 0
    for i in range(n1,n2+1):
        soma += vet[i]
    return soma

def maior(vet):
    maior = float('-inf')
    for i in range(0,9):
        if vet[i] > maior:
            maior = vet[i]
    return maior

def menor(vet):
    menor = float('inf')
    for i in range(0,9):
        if vet[i] < menor:
            menor = vet[i]
    return menor

def soma_posicoes(vet):
    soma = 0
    for i in range(0,9):
        if vet[i] % 2 == 0:
            soma += i
    return soma