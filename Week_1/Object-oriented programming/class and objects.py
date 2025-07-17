class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand}-{self.model}, year {self.year}.")

car1 = Car("Ferrari", "599XX", year=2010)
car2 = Car("Chevrolet", "Camaro", year=2016)

car1.display_info()
car2.display_info()