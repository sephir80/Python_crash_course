class Dog:
    """ Modello di esempio per creazione classe cane"""  # tre doppi apici per docstring come descrittivo della classe

    def __init__(self, name, age):
        """ Inizializza nome ed età attributi """
        self.name = name
        self.age = age

    def sit(self):
        """simula la risposta del cane al comando seduto"""
        print(f"{self.name} è ora seduto.")

    def roll_over(self):
        """Simula il rotolamento del cane"""
        print(f"{self.name} sta rotolando")

    def update_age(self):
        """il cane ha compiuto gli anni"""
        self.age = self.age + 1
        print(f"Tanti auguri {self.name}!!!")


