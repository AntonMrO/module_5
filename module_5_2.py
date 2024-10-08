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
