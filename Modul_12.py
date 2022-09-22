money = int(input("Введите сумму"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for i in per_cent:
    deposit.append(per_cent[i]*money/100)
deposit_max = max(deposit)
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ' + str(deposit_max))

