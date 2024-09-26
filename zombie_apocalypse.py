from human import Human
from zombie import Zombie
from collectible.food import Food
from collectible.water import Water
from collectible.medkit import Medkit
import matplotlib.pyplot as plt
import random
import sys
import time

class __main__:

    def __init__(self): 
        # Set scatter plot size
        FIELD_SIZE_X = 100
        FIELD_SIZE_Y = 100
        
        # Get command line arguments
        if(len(sys.argv) == 4):
            human_count = int(sys.argv[1])
            zombie_count = int(sys.argv[2])
            total_timestep = int(sys.argv[3])
        else:
            human_count = 40
            zombie_count = 40
            total_timestep = 100
        
        # Set number of consumables
        food_count = 10
        water_count = 8
        medkit_count = 8
        
        # Set random coordinates for human
        list_human = [Human(random.randint(20,60),self.generateCoordinates(FIELD_SIZE_X),self.generateCoordinates(FIELD_SIZE_Y)) for _ in range(human_count)]
        # Set random coordinates for zombie
        list_zombie = [Zombie(self.generateCoordinates(FIELD_SIZE_X),self.generateCoordinates(FIELD_SIZE_Y)) for _ in range(zombie_count)]
        # Set random coordinates for food
        list_food = [Food(self.generateCoordinates(FIELD_SIZE_X),self.generateCoordinates(FIELD_SIZE_Y)) for _ in range(food_count)]
        # Set random coordinates for medkit
        list_medkit = [Medkit(self.generateCoordinates(FIELD_SIZE_X),self.generateCoordinates(FIELD_SIZE_Y)) for _ in range(medkit_count)]
        # Set random coordinates for water
        list_water = [Water(self.generateCoordinates(FIELD_SIZE_X),self.generateCoordinates(FIELD_SIZE_Y)) for _ in range(water_count)]
        
        # human move set
        h_moves  = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
        # zombie move set
        z_moves  = [-3,-2,-1,0,1,2,3]
        
        # Get a list of all Consumable's X and Y coordinates
        
        list_x_pos_food = [list_food[i].getX() for i in range(len(list_food))]
        list_y_pos_food = [list_food[i].getY() for i in range(len(list_food))]
        
        list_x_pos_medkit = [list_medkit[i].getX() for i in range(len(list_medkit))]
        list_y_pos_medkit = [list_medkit[i].getY() for i in range(len(list_medkit))]
        
        list_x_pos_water = [list_water[i].getX() for i in range(len(list_water))]
        list_y_pos_water = [list_water[i].getY() for i in range(len(list_water))]
        
        # Set initial timestep
        timestep_count = 0
        
        # Main Timestep Loop
        for i in range(total_timestep):
            # Increment timestep 
            timestep_count = timestep_count + 1

            print("TIME STEP #"+str(timestep_count))
            
            # Control Human movement and interactions
            for human in list_human:
                self.checkInteractionHuman(human,list_human,list_food,list_water,list_medkit,list_zombie)
            
                # Check if human's health falls below 0
                if(human.getHealth() <= 0): 
                    #print("A human has died at age " + str(human.getAge()) + " and timestep " + str(human.getTimestep()))
                    list_human.remove(human)
                    print("A human died, Humans left: ",len(list_human))
                
                # Move Human
                human.move(h_moves,FIELD_SIZE_X,FIELD_SIZE_Y)
            
            # Control Zombie movement and interations
            for zombie in list_zombie:
                self.checkInteractionZombie(zombie,list_human,list_zombie)
                
                # Check if zombie's health falls below 0
                if(zombie.getHealth() <= 0):
                    list_zombie.remove(zombie)
                    print("A zombie died, Zombies left: ",len(list_zombie))
                
                # Move Zombie
                zombie.move(z_moves,FIELD_SIZE_X,FIELD_SIZE_Y)
            
            # Get a list of all Human's X and Y coordinates
            list_x_pos_human = [list_human[i].getX() for i in range(len(list_human))]
            list_y_pos_human = [list_human[i].getY() for i in range(len(list_human))]
        
            # Get a list of all Zombie's X and Y coordinates
            list_x_pos_zombie = [list_zombie[i].getX() for i in range(len(list_zombie))]
            list_y_pos_zombie = [list_zombie[i].getY() for i in range(len(list_zombie))]
            
            # Plot points in the scatter plot
            plt.scatter( list_x_pos_human,list_y_pos_human,50,'green','o',edgecolors='black',alpha=0.75)
            plt.scatter(list_x_pos_zombie, list_y_pos_zombie,50,'red',edgecolors='black',alpha=0.75)
            plt.scatter(list_x_pos_food, list_y_pos_food,50,'brown','s',edgecolors='black',alpha=0.75)
            plt.scatter( list_x_pos_medkit, list_y_pos_medkit,50,'red', 'P',edgecolors='black',alpha=0.75)
            plt.scatter(list_x_pos_water, list_y_pos_water,50,'blue','s',edgecolors='black',alpha=0.75)
            # Set scatter plot's boundaries
            plt.xlim(-5,105)
            plt.ylim(-5,105)
            
            plt.title("Zombie Apocalypse Simulation (TimeStep = " + str(timestep_count) + ")")
            
            plt.pause(0.1)
            plt.clf()
        
        
            
    def checkInteractionZombie(self,zombie,list_human,list_zombie):
        for i in range(zombie.getX()-1,zombie.getX()+2):
            for j in range(zombie.getY()-1,zombie.getY()+2):
                # Zombie zombie Interaction
                for zombie2 in list_zombie:
                    if zombie2.getX() == i and zombie2.getY() == j and zombie.getX() != zombie2.getX() and zombie.getY() != zombie2.getY():
                        zombie.bitesZombie(zombie,zombie2)
    
    def checkInteractionHuman(self,human,list_human,list_food,list_water,list_medkit,list_zombie):
        for i in range(human.getX()-1,human.getX()+2):
            for j in range(human.getY()-1,human.getY()+2):
                # Human food Interaction
                for food in list_food:
                    if food.getX() == i and food.getY() == j:
                        human.setHealth(human.getHealth() + 30)
                        print("A human ate food")
                # Human water Interaction
                for water in list_water:
                    if water.getX() == i and water.getY() == j:
                        human.setHealth(human.getHealth() + 50)
                        print("A human drank water")
                # Human medkit Interaction
                for medkit in list_medkit:
                    if medkit.getX() == i and medkit.getY() == j:
                        human.setHealth(human.getHealth() + 100)
                        print("A human took medkit")
                # Human zombie Interaction
                for zombie in list_zombie:
                    if zombie.getX() ==i and zombie.getY() == j:
                        choice = random.randint(1,10)
                        if choice >= 3:
                            zombie.bitesHuman(human,list_zombie,list_human)
                            return
                        else:
                            human.attacksZombie(zombie,list_zombie)
                # Human human Interaction
                for human2 in list_human:
                    if human2.getX() == i and human2.getY() == j and human.getX() != human2.getX() and human.getY() != human2.getY():
                        choice = random.randint(1,2)
                        if choice == 1:
                            human.attacksHuman(human,human2)
                            if human2.getHealth() <=0:
                                return 
                        else:
                            human.help(human,human2)
                            
    # Generate Random Coordinates                                
    def generateCoordinates(self,field_size):
        return random.randint(0,field_size)
        
# Call main method
if __name__ == "__main__":
    __main__()
        