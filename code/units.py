# units.py
class Unit:
    def __init__(self, name, hp, damage_per_second, attack_speed,
                 attack_radius, cost, speed):
        self.name = name
        self.hp = hp
        self.dps = damage_per_second
        self.attack_speed = attack_speed
        self.attack_radius = attack_radius
        self.cost = cost
        self.speed = speed

class Swordsman(Unit):
    def __init__(self):
        super().__init__("Swordsman", 150, 5, 2, 1, 1, 0.5)

class Archer(Unit):
    def __init__(self, ground_level):
        attack_radius = self.get_attack_radius(ground_level)
        super().__init__("Archer", 50, 20, 10, attack_radius, 2, 1)

    def get_attack_radius(self, ground_level):
        if ground_level == "same":
            return 30
        elif ground_level == "lower":
            return 20
        elif ground_level == "higher":
            return 50

class Catapult(Unit):
    def __init__(self):
        super().__init__("Catapult", 1000, 600, 60, 55, 15, 0.1)

class BatteringRam(Unit):
    def __init__(self):
        super().__init__("Battering Ram", 1500, 400, 15, 1, 15, 0.1)

