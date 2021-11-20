class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self, weight, depth):
        return (self.__length * self.__width * weight * depth) / 1000


road = Road(5000, 20)
print(f'Для заданных характеристик потребуется => {road.calc(25, 5)} т асфальта')




