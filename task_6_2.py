class Road:
    weight_per_meter = 25
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height
    def weight (self):
        return self.__length*self.__width*self.__height*Road.weight_per_meter/1000

l = float(input("Enter length of the road: "))
w = float(input("Enter width of the road: "))
h = float(input("Enter thickness of the road: "))
a = Road(l, w, h)
print(f"The weight of asphalt is {a.weight()} tons.")