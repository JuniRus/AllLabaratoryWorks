class Vechile:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        print(f"Марка: {self.make}; модель: {self.model}")

class Car(Vechile):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        print(f"Марка: {self.make}\nМодель: {self.model}\nТопливо: {self.fuel_type}")

car = Car("Porshe", "Carerra S 911", "бензин")
car.get_info()