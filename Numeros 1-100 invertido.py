numeros=[]

for numero in range(1,101):
    numeros.append(numero)

numerosinvertidos=sorted(numeros, reverse=True)

print(numerosinvertidos)