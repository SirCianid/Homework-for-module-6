class Vehicle:
    __color_variants = ['бирюзовый', 'красный', 'желтый', 'фиолетовый', 'черный']

    def __init__(self, owner, __model,  __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'


    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'


    def get_color(self):
        return f'Цвет: {self.__color}'


    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        new_color = new_color.lower()
        if new_color in self.__color_variants:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Володька', 'Лада "КАЛИНА"', 118, 'желтый')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('белый')
vehicle1.set_color('БиРюЗоВыЙ')
vehicle1.owner = 'Юрец'

# Проверяем что поменялось
vehicle1.print_info()
