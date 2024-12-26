class Car:
    def __init__(self,  car, years, country, price, volume):
        self.car = car
        self.years = years
        self.country = country
        self.price = price
        self.va = volume

    def cars(self):
        return f'car: {self.car} years: {self.years} county: {self.country} price: {self.price} volume: {self.volume}'

c = Car('Mersedes cls 63', 2011, 'Germany', 36100000, 4)
print(c.cars())