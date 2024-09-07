class House:
    houses_history = []

    def __new__(cls, *args):
        # print(args)
        cls.houses_history.append(args[0])      #add NAMES of Class HOUSE in list
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors and new_floor >= 1:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует!')

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории!')

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
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



