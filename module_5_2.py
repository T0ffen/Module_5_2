class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f"The building {self.name} has {self.number_of_floors} \nfloors, going up to the {new_floor} floor")
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor} - there is no such floor')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Name of the building: {self.name}, number of the floors: {self.number_of_floors}"


h1 = House('Lighthouse', 11)
h2 = House('Barn', 2)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
