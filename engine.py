import random
from dice import Dice
from rich import print
from caracter import Warrior, Mage, Thief

def main():
    warrior = Warrior("Tom", 20, 8, 3, Dice(6))
    mage = Mage("Elsa", 20, 8, 3, Dice(6))
    thief = Thief("Patrick", 20, 8, 3, Dice(6))

    cars = [warrior, mage, thief]
    stats = {}
    
    car1 = random.choice(cars)
    cars.remove(car1)
    car2 = random.choice(cars)
    cars.remove(car2)
    
    print(car1)
    print(car2)
    print(cars)
    
    stats[car1.get_name()] = 0
    stats[car2.get_name()] = 1
    
    print(stats)
    
    for i in range(100):
        car1.regenerate()
        car2.regenerate()
        
        while (car1.is_alive() and car2.is_alive()):
            car1.attack(car2)
            car2.attack(car1)
        if car1.is_alive():
            stats[car1.get_name()] += 1
        else:
            stats[car2.get_name()] += 1

    print(stats)
    
if __name__ == '__main__':
    main()

