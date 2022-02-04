from electric_car import Car, ElectricCar

my_new_car = Car("Peugeot", "2008", "2017")

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(50)
my_new_car.read_odometer()
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()


my_tesla = ElectricCar('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
