import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('analys/data.xlsx')
df['Unnamed: 5'].fillna(-1, inplace=True)
df['document'].fillna(-1, inplace=True)
# print(df.columns.to_list())
# ['client_id', 'sum', 'status', 'sale',
# 'new/current', 'Unnamed: 5', 'document', 'receiving_date']
july = df[df['status'] == 'Июль 2021'].index
augst = df[df['status'] == 'Август 2021'].index
# Index([258], dtype='int64') Index([369], dtype='int64')
for_sum = df.iloc[july[0]:augst[0]]
for_sum = (for_sum[for_sum['status'] == 'ОПЛАЧЕНО'])
# print(for_sum[['sum']].sum(axis=0))
# 1) Общая выручка - 859896.47

# За расматривоемый период чего ?
# За весь или из прошлого задания?
for_sum['sum'].plot()
df['sum'].plot()
# 2) plt.show()

september = df[df['status'] == 'Сентябрь 2021'].index
october = df[df['status'] == 'Октябрь 2021'].index
#  Index([484], dtype='int64') Index([594], dtype='int64')
sep_oct = df.iloc[september[0]:october[0]]
total_earnings = sep_oct.groupby('sale')['sum'].sum()
# print("Сотрудник, привлекший больше всех денюжек:", total_earnings.idxmax())
#  3) Смирнов

# december = df.loc[df['status'] == 'Сентябрь 2021'] - Ошибка
oct_dec = df.iloc[october[0]:df.index[-1]]
res = oct_dec['new/current'].value_counts()
# print(res.index[res.argmax()])
# 4) Ответ - текущая


jun = df[df['status'] == 'Июнь 2021'].index  # 129
jun_jul = df.iloc[jun[0]:july[0]]
jun_jul['receiving_date'] = pd.to_datetime(jun_jul['receiving_date'])
df_filtered = jun_jul.query('20210501 < receiving_date < 20210601')
result = df_filtered['document'].value_counts()
# print(result['оригинал'])
# 6) Ответ 1
