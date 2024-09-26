import zombie
import random

class Human():
    
    def __init__(self,age,x,y):
        self.age = age
        self.x = x
        self.y = y
        self.health = 100
        self.timestep = 0
        
    # Getters and Setters
    
    def setX(self,x):
        self.x = x
    
    def setY(self,y):
        self.y = y
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setTimestep(self,timestep):
        self.timestep = timestep
        
    def getTimestep(self):
        return self.timestep
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
        
    def setHealth(self,health):
        self.health = health
    
    def getHealth(self):
        return self.health
        
    # Human attacks zombie
    def attacksZombie(self,zombie,list_zombie):
        list_zombie.remove(zombie)
        print("A human killed a zombie")
    
    # Human attacks human
    def attacksHuman(self,human,human2):
        human.setHealth(human.getHealth()+20)
        human2.setHealth(human2.getHealth()-20)
        print("A human betrayed another human")
    
    # Human helps human
    def help(self,human,human2):
        human.setHealth(human.getHealth()+10)
        human2.setHealth(human2.getHealth()+10)
        print("A human helped another human")
        
    
    def move(self,moves,FIELD_SIZE_X,FIELD_SIZE_Y):
        move_x = random.choice(moves)
        move_y = random.choice(moves)
        next_x = self.getX() + move_x
        next_y = self.getY() + move_y
            
        if next_x < 0:
            next_x = 0
        if next_y < 0:
            next_y = 0
        if next_x >= FIELD_SIZE_X:
            next_x = FIELD_SIZE_X
        if next_y >= FIELD_SIZE_Y:
            next_y = FIELD_SIZE_Y
            
        abs_move_x = abs(move_x)
        abs_move_y = abs(move_y)
        self.setHealth(self.getHealth() - (abs_move_x if abs_move_x >= abs_move_y else abs_move_y))
        self.setAge(self.getAge() + 1)
        self.setTimestep(self.getTimestep() + 1 )
        if(self.getTimestep() > 80): 
            self.setHealth(0)
        self.setX(next_x)
        self.setY(next_y)
        
        #print("Human at "+ str(self.getX()) + ", " + str(self.getY()) + " of age " + str(self.getAge()) + " has Health " + str(self.getHealth()))
    