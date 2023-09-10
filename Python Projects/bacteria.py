# Libraries used
import random
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Data to plot; x is number or cycles Bacteria.passtime in initiated 
# while y is number of bacteria
x = []
y = []

# Creating 'Bacteria'
class Bacteria:

    food = 100000
    population = []    
    name_sig = 0
    pt = 0

    def __init__(self, ident, energy, strength, age):
        self.ident = ident
        self.energy = energy
        self.strength = strength
        self.age = age
        Bacteria.population.append(self)
        Bacteria.name_sig += 1
    
    def eat(self):
        food_am = random.randint(1, 1 + self.strength)
        if Bacteria.food - food_am >= 0 and self.energy > 0:
            self.energy += food_am
            self.strength += random.randint(0,2)
            Bacteria.food -= food_am
        else:
            if self.energy <= 0: 
                self.die()
                #print('Bacteria {} is dead at turn {}.'.format(self.ident, Bacteria.pt))
                Bacteria.population.remove(self)
            else:
                self.energy -= food_am 
                if self.energy <= 0:
                    self.die

    def procreate(self):
        if self.energy % 2 == 0 and self.strength > 3:
            new_bac = Bacteria(str('b' + str(Bacteria.name_sig)), 10, 1, 0)
            self.energy /= 2
            self.strength -= 3
            #print('Bacteria {} created from {} at turn {}.'.format('b' + str(Bacteria.name_sig - 1), self.ident, Bacteria.pt))
    
    def die(self):
        del self
            
    def sort_pop(self):
        sorted(Bacteria.population, self.strength)

    @classmethod
    def pass_time(self):
        for bac in Bacteria.population:
            bac.energy -= int(0.66 * bac.strength)
            bac.eat()
            bac.procreate()
            bac.age += 1   
        Bacteria.pt += 1 
        y.append(len(Bacteria.population))
        x.append(Bacteria.pt)

#Data Interpreting Functions
def eval():
    pop = []
    print('Bacteria Population: ' + str(len(Bacteria.population)))
    print('Food Remaining: ' + str(Bacteria.food))
    print('Number of Turns: ' + str(Bacteria.pt))
    for bac in Bacteria.population:
        pop.append(bac.ident)
    print('Total Cells: ' + str(Bacteria.name_sig))
    print('Surviving Bacteria: ')
    print(pop)  

def by_turn(num_turn):
    for x in range(num_turn):
        Bacteria.pass_time()

def by_end():
    while len(Bacteria.population) > 0:
        Bacteria.pass_time()
        
#Initializing Starting Bacteria
bac0 = Bacteria('b0', 10, 1, 0)

# Calling Time of Trial 
# either until all bacteria are dead BY_END() 
# or for a set ammount of time BY_TURN(INSERT NUMBER OF TURNS)
# by_turn()
by_end()
eval()

#Plot Instructions
plt.plot(x,y)
plt.title('Bacteria Population in Petri Dish')
plt.xlabel('Units of Time')
plt.ylabel('Cell Count')
plt.show()
