'''
Об’єкт “Площина ”
поля
для зберігання рівняння площини;+
методи
введення та виведення коефіцієнтів рівняння площини;+
перевірка належності точки площині;+
знаходження проекції точи на площину;+
знаходження точки перетину прямої з площиною;+
встановлення паралельності з іншою площиною.
'''
import math
class Space():
    def __init__(self,A, B, C, D):
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D
    @property
    def A(self):
        return self.__A
    @A.setter
    def A(self,value):
        self.__A = value

    @property
    def B(self):
        return self.__B
    @B.setter
    def B(self,value):
        self.__B = value

    @property
    def C(self):
        return self.__C
    @C.setter
    def C(self,value):
        self.__C = value

    @property
    def D(self):
        return self.__C
    @D.setter
    def D(self,value):
        self.__D = value

    def point_in_space(self,value):             #Value = x y z
        value = list(map(lambda el: float(el), value.split(sep=' ')))
        verify = self.__A*value[0]+self.__B*value[1]+self.__C*value[2]+self.__D
        if not verify:
            return "Точка належить"
        else:
            return "Не належить"
    def proect_finder(self, point):
        point = list(map(lambda el: float(el), point.split(sep=' ')))
        t = self.__A*self.__A+self.__B*self.__B+self.__C*self.__C
        t = -(point[0]*self.__A+point[1]*self.__B+point[2]*self.__C+self.__D) / t
        point = [t*self.__A+point[0],t*self.__B+point[1],t*self.__C+point[2]]
        return "{0} {1} {2}".format(point[0],point[1],point[2])

    def point_overflow(self,line, A, B, C):
        line = list(map(lambda el: float(el), line.split(sep=' ')))
        t = self.__A * A + self.__B * B + self.__C * C
        t = -(line[0] * self.__A + line[1] * self.__B + line[2] * self.__C + self.__D) / t
        line = [t * A + line[0], t * B + line[1], t * C + line[2]]
        return "{0} {1} {2}".format(line[0], line[1], line[2])

    def paraletion_space(self, A, B, C):
        verify = abs(self.__A*A+self.__B*B+self.C*C) / (math.sqrt(self.__A**2+self.__B**2+self.__C**2)*math.sqrt(A**2+B**2+C**2))
        if verify:
            return 'Площини паралельні'
        else:
            return 'Не паралельні'
s1=Space(1,1,3,2)
print(s1.point_in_space(s1.proect_finder('2 3 5')))
print(s1.point_in_space(s1.point_overflow('1 3 -5',1,2,3)))
print(s1.paraletion_space(1,1,3))