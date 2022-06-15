import random


class Character:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.defense1 = None
        self.heal1 = None
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hitpoints = constitution * 30 + 50

    def printststs(self):
        print_stats = f"player stats are {self.strength},{self.dexterity},{self.constitution},{self.intelligence},{self.wisdom},{self.charisma}"
        return print_stats

    def hitpoints1(self):
        print_hitpoints = f"hitpoint is {self.hitpoints}"
        return print_hitpoints

    def attack(self):
        return random.randrange(1, self.strength)

    def defense(self, defense1):
        self.defense1 = defense1
        a = random.randrange(1, 20)
        if a < self.dexterity:
            return 0
        else:
            self.attack -= defense1
            return self.attack

    def heal(self, heal1):
        self.heal1 = heal1
        self.hitpoints += heal1
        return self.hitpoints


def main():
    my__new__character = Character(15, 15, 15, 15, 15, 15)
    print(my__new__character.printststs())
    print(my__new__character.hitpoints1())
    att = my__new__character.attack()
    print(my__new__character.defense(att))
    print(my__new__character.heal(20))


if __name__ == '__main__':
    main()
