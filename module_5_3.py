class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors and new_floor >= 1:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует!')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.')

    def __eq__(self, other):
        if isinstance(other, House):        #проверка принадлежности классу House
            return self.number_of_floors == other.number_of_floors
        else:
            return f'{other} не явлется объектом класса {House}. Ошибка сравнения'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return f'{other} не явлется объектом класса {House}. Ошибка сравнения'

    def __le__(self, other) :
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return f'{other} не явлется объектом класса {House}. Ошибка сравнения'

    def __gt__(self, other) :
        if isinstance (other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return f'{other} не явлется объектом класса {House}. Ошибка сравнения'

    def __ge__(self, other) :
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return f'{other} не явлется объектом класса {House}. Ошибка сравнения'

    def __ne__(self, other) :
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return f'{other} не явлется объектом класса {House}. Ошибка сравнения'

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += int(other)
        else:
            print(f'Число {other} не целое')
        return self

    def __iadd__(self, other):
        if isinstance (other, int):
            self.number_of_floors += int(other)
        else:
           print(f'Число {other} не целое')
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += int(other)
        else:
            print(f'Число {other} не целое')
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Звездный', 24)

# __str__
print(h1)
print(h2)
print(h3)

# __len__
print(len(h1))
print(len(h2))
print(len(h3))

h3.number_of_floors = 32    #изменен параметр - кол-во этажей
print(h3)

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

#проверка работы на ошибочные данные
h1 += 1.5 # __iadd__
print(h1 < 30) # __lt__
print(h1 == 20)