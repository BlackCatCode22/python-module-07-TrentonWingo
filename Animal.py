class Animal:
    numofanimals = 0

    def __init__(self, species, name, animal_ID, birth_date, color, sex, weight, originating_zoo, date_arrival):
        self.species = species
        self.name = name
        self.animal_ID = animal_ID
        self.birth_date = birth_date
        self.color = color
        self.sex = sex
        self.weight = weight
        self.originating_zoo = originating_zoo
        self.date_arrival = date_arrival
    