class BaseCharacter(object):              #BaseCharacter class is created as a base when the name and life are stored
    
    def __init__(self, name):             # the init method creates variables for life and name 
        self.name= name
        self.life = 100
    
    def printName(self):                  #Create a printname method to print character names 
        print(self.name)

class Weapon(object):                     #create a weapons class
    
    def __init__(self,weaponName):        #the init method creates the string and stores the weapon name
        self.weapon = weaponName
        
    def printWeapon(self):                #the printWeapon method allows the user to print character weapon
        print(self.weapon)
        
class NPC(BaseCharacter):                 #Create a Non Player Class (controlled by computer) which stored methods attack and revive
    
    def __init__(self, name):             # the init method calls the parent class' init method 
        super(NPC,self).__init__(name)    #this init method initializes the base character
        self.attackDamage = 5             #create the attackdamage variable which is set to five 
    def attack(self):                     # attack method allows NPC enemy to damage PC by reducing their health 
        self.life = self.life - self.attackDamage
        
    def printLife(self):                  # print life method prints the current life of any character 
        print(self.life)
        
class PC(BaseCharacter, Weapon):          #Create a PC which is controlled by users and the weapons and stored here
    
    def __init__(self, name, weaponName): # the init method initializes the name and weaponname
        super(PC,self).__init__(name)     # super init initializes the baseCharacter class 
        Weapon.__init__(self,weaponName)  #initiate the weapon class 
               
class Enemy(NPC):                         #Create class enemy which inherits attributes from class NPC
    
    def __init__(self,name):              #initiate the class
        super().__init__(name)            #initiate the NPC class 
                   
         
class Friend(NPC):                        #create class friend which inherits from class NPC
    
    def __init__(self,name,weaponName):   #initiate the class and use the super method to initiate the NPC 
        super(Friend,self).__init__(name) 
             
        

Archer = PC("Aimee","Bow and Arrow")              # create an instance of PC called Archer who uses the weapon knife 
Archer.printName()
Archer.printWeapon()

Butcher = PC("Butcher Witch","Ax")     # create an instance of PC called Archer who uses the weapon knife 
Butcher.printName()
Butcher.printWeapon()

GreenLantern = PC("Michael","Sword")      # create an instance of PC called Archer who uses the weapon knife     
GreenLantern.printName()
GreenLantern.printWeapon()
