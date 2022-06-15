import random


class Character:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hitpoints = constitution * 30 + 50

    def printststs(self):
        print(
            f"player stats are {self.strength},{self.dexterity},{self.constitution},{self.intelligence},{self.wisdom},{self.charisma}")

    def hitpoints1(self):
        print(f"hitpoint is {self.hitpoints}")

    def attack(self):
        attack1 = random.randrange(1, self.strength)
        return attack1

    def defense(self, defense1):
        self.defense1 = defense1
        a = random.randrange(1, 20)
        if (a < self.dexterity):
            return 0
        else:
            b = 0
            b = self.attack()
            b = b - defense1
            return b

    def heal(self, heal1):
        self.heal1 = heal1
        self.hitpoints += heal1
        return self.hitpoints


class MagicCharacter(Character):
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.mana = self.intelligence * 30 + 50

    def printmagicchar(self):
        print(f"the value of mana is{self.mana}")
        super().printststs

    def magicMissile(self):
        a = 0
        a = random.randrange(5, 10)
        self.mana -= 5
        return a

    def fireball(self):
        a = 0
        a = random.randrange(10, 20)
        self.mana -= 10
        return a

    def healMana(self, heal2):
        self.mana += heal2


def main():
    my__new__character = Character(15, 15, 1, 15, 15, 15)
    print(my__new__character.printststs())
    print(my__new__character.hitpoints1())
    att = my__new__character.attack()
    print(my__new__character.defense(att))
    print(my__new__character.defense(att))
    print(my__new__character.defense(att))
    print(my__new__character.heal(20))
    my__new__Magicman = MagicCharacter(15, 10, 1, 15, 15, 15)
    my__new__Magicman.printmagicchar


if __name__ == '__main__':
    main()
