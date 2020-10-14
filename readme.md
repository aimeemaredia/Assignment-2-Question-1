# Question 1 - Inheritance Tree

## Structure

    - Base Class
        - Non player Character
            - Enemy 
            - Friend 
        - Player Character
            - Archer 
            - Butcher
            - Green Lantern 

___

### Base Class

This class contains the name of the character, the health of the character and the method `printName` which prints the name of the character you want. This class is the base to create any character, player or non player in the game. Most attributes of a character are inherited from this class.

___

### Weapon Class

This is another independant class which stores the weapon used by the character it stores the weapon in the string `weaponName` and the `printWeapon` method will print the name of the weapon used by the character.
___

### NPC Class

Class `NPC` inherits from class `BaseCharacter` and also stores the enemy damage number for the enemy. It is stored in the `attackDamage` variable. The method attack is used to attack player characters and reduce their health. The `printLife` method is used to print the updated life of any character.

___

### PC Class

Class `PC` initiates the `BaseCharacter` class and the `Weapon` class to create a player. Instances of this class are the player and a weapon is associated with each one.

___

### Enemy Class

Class `Enemy` initiates the `BaseCharacter` class and instances of this class are NPC.

___

### Friend Class

Class `Friend` initiates the `BaseCharacter` class and instances of this class are NPC.
# Question-1-
