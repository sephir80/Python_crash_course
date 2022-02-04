class Car:
    """semplice tentativo di rappresentare una classe auto"""

    def __init__(self, manufacturer, model, year):
        """inizializza attributi che descrivono una macchina."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0  # percentage

    def get_descriptive_name(self):
        """ritorna il descrittivo formattato e ordinato"""
        long_name = f"{self.manufacturer} {self.model} {self.year}"
        return long_name.title()

    def fill_gas_tank(self):
        """fai il pieno di benzina"""
        self.gas_tank = 100
        print(f"Ho fatto il pieno! Gas tank = {self.gas_tank} [%]")

    def read_odometer(self):
        """stampa il valore del contachilometri attule"""
        print(f"La macchina ha effettuato {self.odometer_reading} ")

    def update_odometer(self, km_fatti):
        """imposta il valore del contachilometri ad un valore passato"""
        if km_fatti < self.odometer_reading:
            print(f"{km_fatti} sono minore dei {self.odometer_reading} gia registrati.Non fare il furbo!")
        else:
            self.odometer_reading = km_fatti

    def increment_odometer(self, km_fatti):
        """incrementare i km del contachilometri ad un valore passato"""
        self.odometer_reading += km_fatti


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """rappresenta aspetto di una macchina, specifica per auto elettrica"""

    def __init__(self, manufacturer, model, year):
        """inizializza attributi della classe parente """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
