def desvioPadrao(valores):
    n = len(valores)
    media = sum(valores) / n
    varianca = (sum([(x - media) ** 2 for x in valores])) / (n -1)
    return varianca ** (1/2) #não pode ser negativo

print(desvioPadrao([5, 2, 11, 8, 3, 8, 7, 4]))