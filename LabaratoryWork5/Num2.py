class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, value):
        self.radius = value

circle = Circle(5)
print("Текущий радиус: {}".format(circle.get_radius()))
circle.set_radius(10)
print(f"Новый радиус: {circle.get_radius()}")