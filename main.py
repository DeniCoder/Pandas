import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students = ['Денис','Евгений','Андрей','Сергей','Владимир','Александр','Алексей','Денис','Максим','Михаил']

objects = ['Математика', 'Русский язык','Английский язык','Немецкий язык','Информатика']

score = np.random.randint(2,6,len(students)*len(objects))

students_repeat = np.repeat(students,len(objects))
objects_repeat = np.tile(objects,len(students))

df = pd.DataFrame({'Студент':students_repeat,'Предмет':objects_repeat,'Оценка':score})

print(df.head())

print(f'Средняя оценка по предметам:{"\n"}',df.groupby(['Предмет'])['Оценка'].mean())

print(f'Медианная оценка по предметам:{"\n"}',df.groupby(['Предмет'])['Оценка'].median())

Q1_math = df[df['Предмет']=='Математика']['Оценка'].quantile(0.25)
Q3_math = df[df['Предмет']=='Математика']['Оценка'].quantile(0.75)
IQR_math = Q3_math - Q1_math
Std_math = df[df['Предмет']=='Математика']['Оценка'].std()
print(f'Первый квартиль по математике:{"\n"}',Q1_math)
print(f'Третий квартиль по математике:{"\n"}',Q3_math)
print(f'Межквартильный размах по математике:{"\n"}',IQR_math)
print(f'Стандартное отклонение по математике: {"\n"}', Std_math)

df.boxplot(column='Оценка',by='Предмет')
plt.show()