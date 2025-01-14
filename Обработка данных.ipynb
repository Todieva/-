import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sqlalchemy import create_engine
from sklearn.impute import KNNImputer

"Профилирование данных"
df = pd.read_excel('/content/Database/Рассеянный склероз_ДСМ.xlsx')
df
"text"

"Проверяем данные"
df.info('/content/Database/Рассеянный склероз_ДСМ.xlsx')

#Переименуем столбцы Объема как в бз для облегчения визиулизации и исключения дальнейших ошибок
df = df.rename(columns={'Объем (цена розн.-уп.розн.), рубли': 'Объем1', 'Объем (розница), упак.': 'Объем2', 'Объем (цена опт.-уп.розн.), рубли': 'Объем3', 'Фирма-производитель': 'Фирма_производитель'})
df

#отсортируем МНН по алфавиту и индексу
df.sort_values(by=['МНН'], inplace=True)
df.index = np.arange(0,3310)
df

# посмотрим на разброс данных
df.describe()

Отрицательных значений не наблюдается.
так как в дальнейшем планируем работать со столбцом отражающий количество проданных в розницу лекарственных средств выраженных в упаковках, то посмотрим на количество МНН, у которых менее 1000 продаж

df['Объем2'].value_counts()


df1 = df[df['Объем2'] >= 1000]
df1['Объем2'].value_counts()

df.duplicated().sum()
Дубликатов нет
Работа с пропусками при просмотре разбраса данных можно убедиться, что отрицательных или пустых числовых значений нет.
# проверяем на наличие пропусков в столбцах по Объемам
filtered_df = df1[(df1['Объем1'] < 1) & (df1['Объем2'] < 1)& (df1['Объем3'] < 1)]
filtered_df
Проверка подтвердила, что пропусков нет в числовых значениях

#проверим: пропущенных значений не осталось
df1.isnull().sum()

# поскольку пропущеные значения только в текстовых столбцах, которые не сильно необходимы для дальнейшего анализа, то
# Заполним пропуски значением из предыдущей строки
df = df.fillna(method='ffill')

# Работа с выбросами 
#нормируем значения
df1_num = df1.select_dtypes('int64')
df1_std = pd.DataFrame()
for col in df1_num.columns:
    n = df1_num[col].mean()
    s = df1_num[col].std()
    df1_std[col + '_n'] = (df1_num[col] - n) / s
df1_std.head(10)

# визуализируем ящик с усами, чтобы оценить количество выбросов
fig = plt.figure(figsize =(20,5))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xticklabels(df1_std.columns)

data = []
for col in df1_std.columns:
    data.append(df1_std[col])

bp = ax.boxplot(data, widths=0.5)
plt.show()

# для каждого столбца, кроме столбцов год и месяц пропишем цикл, в котором значениям, выходящим за интерквартилный размах будет присваиваться NaN
for x in ['Объем1']:
    q75,q25 = np.percentile(df1.loc[:,x],[75,25])
    intr_qr = q75-q25

    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)

    df1.loc[df1[x] < min,x] = np.nan
    df1.loc[df1[x] > max,x] = np.nan

for x in ['Объем2']:
    q75,q25 = np.percentile(df1.loc[:,x],[75,25])
    intr_qr = q75-q25

    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)

    df1.loc[df1[x] < min,x] = np.nan
    df1.loc[df1[x] > max,x] = np.nan

for x in ['Объем3']:
    q75,q25 = np.percentile(df1.loc[:,x],[75,25])
    intr_qr = q75-q25

    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)

    df1.loc[df1[x] < min,x] = np.nan
    df1.loc[df1[x] > max,x] = np.nan

# но теперь появились нулевые значения, с которым проведём аналогичную работу
df1.isnull().sum()

#заполняем образовавшиеся пропуски
df_num3 = df1.select_dtypes('float64')
imputer = KNNImputer(n_neighbors=5, weights='uniform') #создаем импьютер
imputer.fit(df_num3)
df_num3 = pd.DataFrame(imputer.transform(df_num3), index=df_num3.index, columns=df_num3.columns) #заполняем недостающие значения
df_num3

#перезапишем в рабочий датафейм
df1['Объем1']=df_num3['Объем1']
df1['Объем2']=df_num3['Объем2']
df1['Объем3']=df_num3['Объем3']

#проверка: нулевых значений больше нет (Цена в это число пока не должна входить, т к она создается в следующей строке)
df1.isnull().sum()

Создадим новый столбец "Цена", чтобы узнать стоимость препаратов, для этого в столбеце делим строки с Объем (цена опт.-уп.розн.), рубли на Объем (розница), упак.
df1['Цена'] = df1['Объем3']/df1['Объем2']

# для каждого ценнового сегмента создадим новую колонку, в которую будем записывать соотвествует ли числовое значение данному сегменту
def check(col):
  res = []
  for i in col:
    if i < 1500:
      res.append('недостаток')
    elif i < 5000:
      res.append('входит')
    else:
      res.append('избыток')
  return res

df1.loc[:, 'Свыше_1500'] = check(df1['Цена'])

df1['Свыше_1500'].value_counts()

def check(col):
  res = []
  for i in col:
    if i < 500:
      res.append('недостаток')
    elif i < 1500:
      res.append('входит')
    else:
      res.append('избыток')
  return res

df1.loc[:, 'размер_500до1500'] = check(df1['Цена'])

def check(col):
  res = []
  for i in col:
    if i < 1:
      res.append('недостаток')
    elif i < 500:
      res.append('входит')
    else:
      res.append('избыток')
  return res

df1.loc[:, 'до_500'] = check(df1['Цена'])

df1['размер_500до1500'].value_counts()

df1['до_500'].value_counts()

#Исследовательский анализ данных

def analyze_data(df1):
    print("\n Анализ данных \n")
# Анализ по Лекарственной формы
print("Лекарственная форма:")
print(df['Лекарственная форма'].value_counts().head())
print("\n")
# Анализ по Брендам
print("Распределение Брендов по упоминанию:")
print(df['Бренд'].value_counts())
print("\n")

# Анализ по МНН
print("Распределение по МНН:")
print(df['МНН'].value_counts())
print("\n")

# Анализ по годам
print("Топ годов:")
print(df['Год'].value_counts().head())

Оформление Дашборда
#посмотрим на корреляцию принаков между собой, возможно это поможет в дальнейшем анализе
plt.figure(figsize=(12,10), dpi=80)
sns.heatmap(df1_num.corr(method='spearman'), xticklabels=df1_num.corr(method='spearman').columns, yticklabels=df1_num.corr(method='spearman').columns, cmap='coolwarm', center=0, annot=True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

def create_visualizations(df1):

 # График 1: Распределение Объема (розница), упак. по  МНН
plt.figure(figsize=(10, 6))
sns.countplot(data=df1, x='МНН')
plt.xticks(rotation=45)
plt.title('Объем2 of МНН')
plt.tight_layout()
plt.show()

# График 2: Распределение упоминания Объем (цена опт.-уп.розн.), рубли по годам
plt.figure(figsize=(10, 6))
sns.countplot(data=df1, x='Год')
plt.xticks(rotation=45)
plt.title('Объем1, by Год')
plt.tight_layout()
plt.show()

# График 3: Общая ависимость упоминания МНН
plt.figure(figsize=(12, 10))
df1['МНН'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of МНН')
plt.tight_layout()
plt.show()

Определение метрик
def calculate_quality_metrics(df1):
  metrics = {
        'total_rows': len(df1),
        'total_columns': len(df1.columns),
        'missing_values': df1.isnull().sum().to_dict(),
        'duplicates': len(df1) - len(df1.drop_duplicates()),
        'completeness': (1 - df1.isnull().sum() / len(df1)).to_dict(),
        'unique_values': df1.nunique().to_dict()
    }
print(metrics)

#Сохраняем измененный файл
df1.to_csv('/content/Database/clean_data.csv', sep=';', encoding='utf-8-sig')
from csv import reader
# Установить соединение с базой данных
conn = sqlite3.connect('/content/Database/clean_db.sqlite3')
c = conn.cursor()

 # Создаем таблицу analytics
c.execute( '''CREATE TABLE analytics(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Тип товара TEXT,
Полное наименование TEXT,
МНН TEXT,
Лекарственная форма TEXT,
Бренд TEXT,
Фирма_производитель TEXT,
Корпорация TEXT,
Фармакотерапевтическая группа TEXT,
АТС1 TEXT,
АТС2 TEXT,
АТС3 TEXT,
АТС4 TEXT,
АТС5 TEXT,
Ephmra1 TEXT,
Ephmra2 TEXT,
Ephmra3 TEXT,
Ephmra4 TEXT,
Год INTEGER,
Месяц INTEGER,
Объем1 INTEGER,
Объем2 INTEGER,
Объем3 INTEGER,
Cвыше_1500 TEXT,
размер_500до1500 TEXT,
до_500 TEXT,
Цена TEXT)''')

# Вставка данных в таблицу
data = []

with open('/content/Database/clean_data.csv', encoding='utf-8') as f:
    read = reader(f, delimiter=';')
    read.__next__()
    for line in read:
        chunk = []
        chunk.append(line[1])
        chunk.append(line[2])
        chunk.append(line[3])
        chunk.append(line[4])
        chunk.append(line[5])
        chunk.append(line[6])
        chunk.append(line[7])
        chunk.append(line[8])
        chunk.append(line[9])
        chunk.append(line[10])
        chunk.append(line[11])
        chunk.append(line[12])
        chunk.append(line[13])
        chunk.append(line[14])
        chunk.append(line[15])
        chunk.append(line[16])
        chunk.append(line[17])
        chunk.append(int(line[18]))
        chunk.append(float(line[19]))
        chunk.append(float(line[20]))
        chunk.append(float(line[21]))
        chunk.append(float(line[22]))
        chunk.append(line[23])
        chunk.append(line[24])
        chunk.append(line[25])
        chunk.append(line[26])
        data.append(chunk)

with conn:
    c.executemany(
        '''
        INSERT INTO analytics VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        data
    )
