class Animals:
    def get_type(self):
        return "This is an animal."

class Herbivores(Animals):
    def get_type(self):
        return "This is a herbivore."

class Carnivores(Animals):
    def get_type(self):
        return "This is a carnivore."

class WarmBlooded(Animals):
    def get_type(self):
        return "This is a warm-blooded animal."

class CoolBlooded(Animals):
    def get_type(self):
        return "This is a cool-blooded animal."

class Artiodactyls(Herbivores, WarmBlooded):
    pass

class Cows(Artiodactyls):
    pass

class Bears(Herbivores, Carnivores, WarmBlooded):
    pass

class BrownBear(Bears):
    pass

class GrizzlyBear(Bears):
    pass

class Snakes(CoolBlooded, Carnivores):
    pass

class Poisonous(Snakes):
    pass

class Cobra(Poisonous):
    pass

class NonPoisonous(Snakes):
    pass

class Adder(NonPoisonous):
    pass

cobra = Cobra()
brown_bear = BrownBear()

print(cobra.get_type())
print(brown_bear.get_type())
