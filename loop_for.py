"""
loop e for
qtd = int(input('quantas vezes o loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num =  int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'a soma é `{soma}')
"""
qtd = int(input('qual numero de habitantes? '))
valor = int(input('qual valor do kwh? '))
soma = 0
residencial = []
comercial = []
industrial = []
for n in range(1, qtd+1):
    num =  int(input(f'Informe o {n}/{qtd} valor: '))
    tipo = int(input(f'Informe o codigo: '))
    if tipo == 1:
        residencial.append(num)
    if tipo == 2:
        comercial.append(num)
    if tipo == 1:
        industrial.append(num)
    else:
        print(f'valor invalido')
total = (residencial + comercial + industrial)
media = sum(total)*valor/qtd

print(f'valor max: {max(total)*valor}')
print(f'valor min: {min(total)*valor}')
print(f'valor médio: {media}')
print(f'valor residencial: {sum(residencial)*valor}')
print(f'valor comercial: {sum(comercial)*valor}')
print(f'valor industrial: {sum(industrial)*valor}')

