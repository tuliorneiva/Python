import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
apre = [a1, a2, a3, a4]
random.shuffle(apre)
print(f'A odem de apresentação será:', end=' ')
print(apre)
