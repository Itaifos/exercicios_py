# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

print("O programa verifica se o numero digitado pertence a sequência de fibonacci")   
numero_informado = int(input("Digite um numero: "))

def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)

def verifica_fib():
    for i in range(numero_informado, -1, -1):
        if numero_informado == rec_fib(i):
            return True
        
    return False

if verifica_fib() == True:
    print("O numero faz parte da sequência de fibonacci")
else:
    print("O numero não faz parte da sequência de fibonacci")