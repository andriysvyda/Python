"""Об’єкт “Аудыо файл”
поля:
формат файлу;+
дата створення;+
тривалість;+
частота дискретизації;+
глибина кодування;+
методи
визначення «віку» файлу;+
визначення кількості точок збереження за вказаний проміжок часу;
визначення об’єму файлу з вказаною тривалістю.

"""
from datetime import date, datetime
def get_today_date():
    return date(datetime.today().year, datetime.today().month, datetime.today().day)
class audiofile():
    def __init__(self,formatfily, data_st, truvalist, chas_d, glybina_cod):
        self.formatfily = formatfily
        self.data_st = data_st
        self.truvalist = truvalist
        self.chas_d = chas_d
        self.glybina_cod = glybina_cod
    def age(self):
        return get_today_date().year - self.data_st.year
    data_st=date(2019, 5, 16)
AudioFile = audiofile(input('Формат Файлу: '), input('Дата створення: '), input('Тривалість запису: '),
float(input('Частота Дискритизації: ')), input('Глубина кодування: '))
print(" Формат файлу: {0}\n Дата створення: {1}\n Тривалість запису: {2}\n Частота Дискритизації: {3:.2f}\n Глубина Кодування {4}\n"
      .format(AudioFile.formatfily, AudioFile.data_st, AudioFile.truvalist, AudioFile.chas_d, AudioFile.glybina_cod))
