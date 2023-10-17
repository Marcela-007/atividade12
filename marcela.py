 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("Insira o ano desejado: "))
if (ano %4==0 and ano %100!=0) or (ano %400==0):
   print("O ano inserido é bissexto")
else:
   print("O ano inserido não é bissexto")