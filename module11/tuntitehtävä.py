class Adventurer:
    def __init__(self, adventureName, healthPoints=100, stamina=100, attackDamage=10, myParty:list=[]):
        self.healthPoints = healthPoints
        self.stamina = stamina
        self.attackDamage = attackDamage
        self.adventureName = adventureName
        self.myParty = myParty

    def gain_life(self, amount):
        self.healthPoints += amount

    def lose_life(self, amount):
        self.healthPoints -= amount
        if self.healthPoints < 0:
            self.healthPoints = 0

class Mage(Adventurer):
    def __init__(self, adventureName, healthPoints=50, stamina=100, attackDamage=20):
        super().__init__(adventureName, healthPoints, stamina, attackDamage)

    def party_heal(self):
        for i in self.myParty:
            i.gain_life(50)

class Paladin(Adventurer):
    def __init__(self, adventureName, healthPoints=150, stamina=100, attackDamage=5):
        super().__init__(adventureName, healthPoints, stamina, attackDamage)

class Rogue(Adventurer):
    def __init__(self, adventureName, healthPoints=100, stamina=100, attackDamage=10):
        super().__init__(adventureName, healthPoints, stamina, attackDamage)


class Party:
    def __init__(self, partyList:list=[]):
        self.partyList = partyList
        for i in partyList:
            i.myParty = partyList

    def add_member(self, member:Adventurer):
        self.partyList.append(member)
        member.myParty = self.partyList

    def retire__member(self, member:Adventurer):
        self.partyList.remove(member)
        member.myParty = []

    def show_members(self):
        for i in self.partyList:
            print(f"Name: {i.adventureName}")

    def show_health(self):
        for i in self.partyList:
            print(f"Name: {i.adventureName}, Health: {i.healthPoints}")


rogue = Rogue("Aseo")
mage = Mage("Raven")
paladin = Paladin("Jack")

party1 = Party([rogue, mage, paladin])

party1.show_members()
party1.show_health()
print("")
paladin.lose_life(100)
mage.lose_life(20)
rogue.lose_life(50)

party1.show_health()
print("")
mage.party_heal()

party1.retire__member(mage)

party1.show_members()
party1.show_health()