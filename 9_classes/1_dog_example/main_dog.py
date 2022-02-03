from dog import Dog

my_dog = Dog("Ocra", 2)

my_dog.sit()
my_dog.roll_over()


print(f"{my_dog.name} ha {my_dog.age} anni")

my_dog.update_age()

print(f"{my_dog.name} ha {my_dog.age} anni")
