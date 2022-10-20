from random import randint

class gracz:

    def __init__(self, armor, name):
        self.name = name
        self.healtpoints = 100
        self.armor = armor
        print(self.name, "has currently ", self.healtpoints, "Hp")
        
    def attack(self, atack, enemy):
        '''attack on other player
        '''
        
        print(self.name, "you were hit !")
        hit = (atack - self.armor)
        self.healtpoints = self.healtpoints - hit
        print(enemy, "gave you ", hit, "dmg")
        print(self.name, "you still have :", self.healtpoints,"Hp\n")
        # return self.healtpoints
        if(self.healtpoints < 1):
            return "defeat"

    def __str__(self):
        return "the first to lose all hp points loses the game"


player1 = input("enter the name of the first player: \n")
player2 = input("enter the name of the second player: \n")
print("\n")

p1 = gracz(randint(1, 10), player1)
p2 = gracz(randint(1, 10), player2)
print("\n")

for _ in range(30):
    hit_Or_no_hit = randint(0, 1)
    if(hit_Or_no_hit == 1):
        if(p2.attack(randint(10, 20), p1.name) == "defeat"):
            print(p2.name, "you have been defeated")
            break

    elif(hit_Or_no_hit == 0):
        if(p1.attack(randint(10, 20), p2.name) == "defeat"):
            print(p1.name, "you have been defeated")
            break
