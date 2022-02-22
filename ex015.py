d = int(input('Quantos dias alugados? '))
k = float(input('Quantos kilometros rodados? '))
a = 60 * d
b = 0.15 * k
print(f'O total a pagar é R${a+b:.2f}')
