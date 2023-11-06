# Exercício Python 22: Faça um programa que mostre na tela os numeros pares entre 1 e 50 (dica estude range e seus paramentros)
numero = (range(1, 51))
for numeros in numero:
    if numeros % 2 == 0:
        print(numeros)