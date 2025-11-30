#Author:Rinat.R
#Date:11.15.25
#Problem 5:
"""creates a character and prints their weapons and weaknesses"""

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weakness(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


player1 = Character('nickname', 'weapons', 'weaknesses')
player1.nickname = 'dragon slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']


for item in player1.weapons:
    print('item', item)

for debuff in player1.weaknesses:
    print('debuff', debuff)


task1_list = ['rope', 'coat', 'first aid kit']
task_weak = ['slow']

for item in player1.weapons:
    print('item', item)
else:
    print('item not in the master list')

