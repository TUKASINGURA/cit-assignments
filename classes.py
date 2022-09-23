class Animal:
    def __init__(self,color,breed,young_one):
        self.color= color
        self.breed= breed
        self.young_one= young_one
    def __repr__(self):
        return f"the animal is a {self.color} {self.breed} and its young_one is {self.young_one} "
class Cow(Animal):
    def __init(self,color,breed,young_one,owner):
        self.owner=owner
        super().__init__(color,breed,young_one)
    def color(self):
        print(f"the color is {self.color}")
    def breed(self):
        print(f"the breed of the animal is {self.breed}")
    def youngone(self):
        print(f"the young one of the animal is {self.young_one}")    
girraffe = Animal("brown","local","girraffe")
# print(girraffe())
cow = Cow("Exotic","calf","calf","Richard")