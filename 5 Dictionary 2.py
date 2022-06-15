import random

thisdic = {
    "strength": 12,
    "dexterity": 12,
    "constitution": 14,
    "intelligence": 15,
    "wisdom": 20,
    "charisma": 15
}
value = {}
for a in thisdic.keys():
    value[a] = random.randrange(1, 20)
print(value)
