
print("O programa verifica se o numero digitado pertence a sequência de fibonacci")   
numero_informado = int(input("Digite um numero: "))

def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)

def verifica_fib():
    i = 0
    while True:
        fib_i = rec_fib(i)
        if fib_i >= numero_informado:
            break
        i += 1
    
    if fib_i == numero_informado:
        print("O numero faz parte da sequência de fibonacci")
    else:
        print("O numero não faz parte da sequência de fibonacci")
    
verifica_fib()