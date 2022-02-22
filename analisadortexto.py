class Pessoa:
    nome = input('Qual o nome da pessoa? ')
    idade = input('Qual a idade da pessoa? ')

pessoa = Pessoa()

print('A pessoa tem um nome? ', hasattr(pessoa, 'nome'))
print('A pessoa trabalha? ', hasattr(pessoa, 'trabalho'))
