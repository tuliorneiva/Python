nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print('Seu nome tem ', len(nome) - nome.count(' '), 'letras.')
separa = nome.split()
print(f'seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
