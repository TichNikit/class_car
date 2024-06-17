class Vehicle:
    __COLOR_VARIANTS = ['green', 'black', 'red', 'blue']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        get_model_str = f'Модель: {self.__model}'
        return get_model_str

    def get_horsepower(self):
        get_horsepower_str = f'Мощность двигателя: {self.__engine_power}'
        return get_horsepower_str

    def get_color(self):
        get_color_str = f'Цвет: {self.__color}'
        return get_color_str

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


car_1 = Vehicle('Say my name', '1', 100, 'green')
print(car_1.get_model())
print(car_1.get_horsepower())
print(car_1.get_color())
car_1.print_info()
car_1.owner = 'Tell my name'
print(car_1.owner)
car_1.__model = '2'
print(car_1.__model)
car_1.set_color('BLACK')
print(car_1.get_color())


car_2 = Sedan('Name', '10', 200, 'blue')

print(car_2.get_model())
print(car_2.get_horsepower())
print(car_2.get_color())
car_2.print_info()
car_2.owner = 'Tell'
print(car_2.owner)
car_2.__model = '20'
print(car_2.__model)

print(car_1._Vehicle__COLOR_VARIANTS)
print(car_2._Vehicle__COLOR_VARIANTS)
print(car_2._Sedan__PASSENGERS_LIMIT)