import pandas as pd
"""Задание:

За каждую заключенную сделку менеджер получает бонус, который рассчитывается
следующим образом.

1) За новые сделки менеджер получает 7 % от суммы, при условии, что статус
оплаты «ОПЛАЧЕНО», а также имеется оригинал подписанного договора с
клиентом (в рассматриваемом месяце).


2) За текущие сделки менеджер получает 5 % от суммы, если она больше 10 тыс.,
и 3 % от суммы, если меньше. При этом статус оплаты может быть любым,
кроме «ПРОСРОЧЕНО», а также необходимо наличие оригинала подписанного
договора с клиентом (в рассматриваемом месяце).
Бонусы по сделкам, оригиналы для которых приходят позже рассматриваемого
месяца, считаются остатком на следующий период, который выплачивается по мере
прихода оригиналов. Вычислите остаток каждого из менеджеров на 01.07.2021."""
# ['client_id', 'sum', 'status', 'sale',
# 'new/current', 'Unnamed: 5', 'document', 'receiving_date']
df = pd.read_excel('analys/data.xlsx')
df.rename(columns={'new/current': 'new_current'}, inplace=True)
july = df[df['status'] == 'Июль 2021'].index
for_sum = df.iloc[df.index[1]:july[0]]
result1 = for_sum[(for_sum.status == 'ОПЛАЧЕНО') &
                  (for_sum.document == 'оригинал')]
result1 = result1[result1.new_current == 'новая']
total_earnings1 = result1.groupby('sale')['sum'].sum().reset_index()
total_earnings1['bonus'] = total_earnings1['sum'] * 0.07
print(total_earnings1)

result_2 = for_sum[(for_sum.status != 'ПРОСРОЧЕНО') &
                   (for_sum.document == 'оригинал')]
result_2 = result_2[result_2.new_current == 'текущая']
total_earnings2 = result_2.groupby('sale')['sum'].sum().reset_index()
total_earnings2['bonus'] = total_earnings2['sum'] * 0.05
print(total_earnings2)


# Если честно не уверен что правильно сделал задание ヾ(⌐■_■)ノ♪
