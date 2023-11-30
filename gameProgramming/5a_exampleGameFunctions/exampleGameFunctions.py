# Example Game Functions Project, Xavier Oliver, v0.5
import random
skillList = ['fireball', 'icebeam', 'thunderbolt','sword slash', 'kamikaze', 'heal', 'guard', 'dark void', 'holy wrath']
enemyList = ['Goblin', 'Goblin Soldier', 'Goblin Chief', 'Skeleton Knight', 'Haunted Armor', 'Undead Wizard', 'Dragon', 'Hydra']
itemList = ['potion', 'antidote', 'fire-boost', 'ice-boost', 'thunder-boost', 'dark-boost', 'light-boost', 'revival totem']
playerHealth = 150
def generatePlayerStats(): # Generates player stats. No parameters required. 
    stats = []
    stats.append(random.randint(1, 30)) # Strength
    stats.append(random.randint(1, 30)) # Defense
    stats.append(random.randint(1, 30)) # Speed
    stats.append(random.randint(1, 30)) # Accuracy
    stats.append(random.randint(1, 15)) # Luck
    print(f"Strength: {stats[0]}")
    print(f"Defense: {stats[1]}")
    print(f"Speed: {stats[2]}")
    print(f"Accuracy: {stats[3]}")
    print(f"Luck: {stats[4]}")
    return stats # Returns the stats list.
    
statsList = generatePlayerStats() # Outputs returned list to a new variable
#print(statsList[1])
def damageCalc(skillUsed, enemyAttackValue, defense = statsList[1]): # Calculates how much damage the player took. Requires the enemy's attack stat, the skill used by the player, and the player's defense value from the previous function.
    damageTaken = enemyAttackValue - defense
    if damageTaken <= 0:
        damageTaken = 0
        print('You took no damage.')
    elif skillUsed == 'guard':
        guardActive = True
        if guardActive == True:
            damageTaken /= 2
        if type(damageTaken) == float:
            damageTaken = round(damageTaken)
            damageTaken = int(damageTaken)
            print(f'Since guard was active, you took {damageTaken} damage.')
    else:
        print(f'You took {damageTaken} damage.')
    return damageTaken # Returns player's health.
    
def enemySelect(): # Chooses a random enemy and amount of enemies. No parameters required.
    i = random.randint(0, len(enemyList) - 1)
    enemyAmount = random.randint(1, 5)
    enemy = enemyList[i]
    if enemyAmount == 1:
        print(f'You encountered {enemyAmount} {enemy}.')
    else:
        print(f'You encountered {enemyAmount} {enemy}s.')
    
        
def namePlayer(): # Obtains character's name from user input. No parameters. 
    name = input('Name your character.')
    nameConfirm = int(input(f'Your input name is {name}, correct? \nPlease input either yes(1) or no(2).'))
    if nameConfirm == 1:
        print('Character name confirmed.')
    else:
        name = input('Please re-input the name of your character.')
        print('Character name confirmed.')
    return name # Returns name of character.
playerName = namePlayer()

def playerTurn(playerCurrentHealth): # Determines if the player can make their turn, then sees what skill they use. Requires player health. Returns skill used.
    while playerHealth > 0:
        print(skillList)
        skill = input(f'{playerName}, please select an action from your skill list.\n').lower() # Lines 59 - 62 based on code from https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
        count = skillList.count(skill)
        #print(count)
        if count > 0:
                print(f'You used {skill}.')
                break
        else:
            print('Chosen skill not found.')
            continue
    return skill

def gameOver(playerCurrentHealth): # Checks to see if the player's health is less than or equal to zero, then tells them the game has ended. Requires player's current health. No return.
    if playerCurrentHealth <= 0:
        print('You have lost all of your health. \nGame Over.')

def criticalHit(skillUsed, playerDamageDealt): # Checks to see if the player lands a crit, and determines the strength of that crit. Requires the skill used and how much damage the player dealt.
    critMultiplier = 1.50
    if skillUsed != 'guard':
        critRoll = random.randint(1, 100)
        if critRoll >= 85:
            critSuccess = True
            if statsList[4] >= 10:
                critMultiplier = 2.0
                playerDamageDealt *= critMultiplier
                if type(playerDamageDealt) == float:
                    playerDamageDealt = round(playerDamageDealt)
                    playerDamageDealt = int(playerDamageDealt)
                    print(f'Because of your high luck, you landed a strong critical hit. \nYou dealt {playerDamageDealt} damage.')
                else:
                    print(f'Because of your high luck, you landed a strong critical hit. \nYou dealt {playerDamageDealt} damage.')
            elif statsList[4] < 10:
                playerDamageDealt *= critMultiplier
                if type(playerDamageDealt) == float:
                    playerDamageDealt = round(playerDamageDealt)
                    playerDamageDealt = int(playerDamageDealt)
                    print(f'You landed a critical hit. \nYou dealt {playerDamageDealt} damage.')
        else:
            critSuccess = False
    return playerDamageDealt # Returns the amount of damage dealt, post crit

def playerItemChoose(): # Checks to see if a chosen item is in the itme list, then tells the player they used that item. No parameters.
    print(itemList)
    item = input(f'{playerName}, please select an item from your inventory.\n').lower()
    # count = itemList.count(item)
    for i in range(len(itemList) - 1):
        if item == itemList[i]:
                print(f'You used {item}.')
                break
        else:
            print('Chosen item not found.')
            continue
    return item # Returns the used item.

enemySelect()
playerItem = playerItemChoose()
skillUsed = playerTurn(playerHealth)
criticalHit(skillUsed, 23)
playerDamage = damageCalc(skillUsed, 45)
playerHealth -= playerDamage
gameOver(playerHealth)


# Code Review by Noah Mulder