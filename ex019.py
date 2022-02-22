from random import choice
aluno1 = input('Digite o nome primeiro aluno: ')
aluno2 = input('Digite o nome segundo aluno: ')
aluno3 = input('Digite o nome terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
print(f'O aluno escolhido foi {choice([aluno1, aluno2, aluno3, aluno4])}')
