qtd_cds = int(input('Digite quantos CDs tem a sua coleção: '))
valor_total = float(input('Digite o valor do CD: '))

for _ in range (qtd_cds - 1):
    valor_cd = float(input('Digite o valor do CD: '))
    valor_total = valor_total + valor_cd

media_cds = (valor_total) / (qtd_cds)

print(f'A média do valor gasto em cada um deles: é R${media_cds}')