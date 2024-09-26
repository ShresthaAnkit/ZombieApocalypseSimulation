import random

class Zombie():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 100
    
    # Getters and Setters
    
    def setHealth(self,health):
        self.health = health
        
    def getHealth(self):
        return self.health
        
    def setX(self,x):
        self.x = x
    
    def setY(self,y):
        self.y = y
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def move(self,moves,FIELD_SIZE_X,FIELD_SIZE_Y):
        next_x = self.getX() + random.choice(moves)
        next_y = self.getY() + random.choice(moves)
            
        if next_x < 0:
            next_x = 0
        if next_y < 0:
            next_y = 0
        if next_x >= FIELD_SIZE_X:
            next_x = FIELD_SIZE_X
        if next_y >= FIELD_SIZE_Y:
            next_y = FIELD_SIZE_Y
            
        self.setX(next_x)
        self.setY(next_y)  
        #print("Zombie at "+ str(self.getX()) + ", " + str(self.getY()) + " has Health " + str(self.getHealth()))
    
    # Zombie bites human
    def bitesHuman(self,human,list_zombie,list_human):
        zombified = Zombie(human.getX(),human.getY())
        list_zombie.append(zombified)
        zombified.setHealth(human.getHealth())
        list_human.remove(human)
        print("A human zombified")
        
    # Zombie bites zombie    
    def bitesZombie(self,zombie,zombie2):
        zombie.setHealth(zombie.getHealth() - 10)
        zombie2.setHealth(zombie2.getHealth() - 10)
        print("A zombie bit another zombie")

        