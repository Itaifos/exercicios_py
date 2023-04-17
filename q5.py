nome = "sofiati"
reverso = ""

for i in range(len(nome)-1, -1, -1):
    reverso += nome[i]

print(reverso)