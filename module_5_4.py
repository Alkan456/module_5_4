
class House:

    House_history = []

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        args = args[0]
        cls.House_history.append(args)
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        if isinstance(number_of_floors, House):
            self.houses_history = number_of_floors.append()

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor +1):
                print(floor)
        else:
                print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        return print(f'{self.name} Снесён, но он остаётся в истории' )










house1 = House('ЖК Эльбрус', 10)
print(House.House_history)
house2 = House('ЖК Акация', 20)
print(House.House_history)
house3 = House('ЖК Матрёшки', 20)
print(House.House_history)

del house2
del house3
print(House.House_history)