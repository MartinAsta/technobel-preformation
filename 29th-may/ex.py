'''
Exercice récapitulatif : Heroes Vs Monsters
Bienvenue dans la forêt de « Shorewood », forêt enchantée du pays de « Stormwall ».
Dans cette forêt, se livre un combat acharné entre les héros d’une part et les monstres d’autre part.
Notre rôle est de donner vie à cette forêt au travers d’un programme écrit en console reprenant tous
les concepts orientés objets vu au cours.
Décrivons, un peu ce monde, nous retrouvons deux familles de personnages, les héros : Humain ou
nain et les monstres : Loup, Orque ou dragonnet.
Chaque personnage possède différentes caractéristiques :
 Endurance (End),
 Force (For),
 Points de vie (PV)
La force et l’endurance sont calculées à la création du personnage en lançant, pour chacune d’elles,
quatre dé 6 faces et en n’en reprenant que les 3 meilleurs.
Les points de vie sont déterminés par l’endurance additionnée avec le modificateur1 basé sur
l’endurance.
Les personnages ont une action Frappe. Lorsqu’un personnage frappe sur un autre, les dégâts sont
déterminés par le jet d’un dé à 4 faces auquel on ajoute un modificateur1 basé sur la caractéristique
de Force. Une fois calculé, les dégâts sont retirés des points de vies de la cible.
Les héros en tuant les monstres vont les dépouiller de leur richesse (Or et/ou Cuir)
2
, qu’ils vont
stocker sans limite.
Après chaque combat les héros se reposent et restaurent leurs points de vie et affronte le monstre
suivant jusqu’à leur mort3
.
Nous avons deux types de héros, les humains qui ont +1 aux caractéristiques de Force et d’Endurance
et les nains qui ont plus 2 en Endurance.
Ensuite nous avons les monstres :
 Les loups :
o Ils peuvent être dépecés (donne du cuir).
 Les orques :
o Ils ont +1 en force
o Ils ont de l’or
 Les dragonnets :
o Ils ont +1 en endurance
o Ils ont de l’or
o Ils peuvent être dépecés (donne du cuir).
Contrainte :
 La force et l’endurance sont des propriétés en lecture seule.
 La propriété PV est
(Si les délégués ont été vu)
 « private » aussi bien en lecture et en écriture.
(sinon)
 en lecture seule.
 Les bonus d’endurance et de force offerts par les classes (Humain, Nain, Orque et Dragonnet)
ne doivent pas modifier la caractéristique de base du personnage.
 La classe dé contient deux propriétés en lecture seule Minimum et Maximum ainsi qu’une
méthode Lance qui retourne un entier aléatoire4
.
Exercice supplémentaire :
Prévoir une zone de jeu de 15 sur 15, contenant une 10aine de monstres espacés d’au moins de 2
cases (horizontale et verticale) les uns des autres.
Pour ce faire, ajouter aux personnages deux propriétés X et Y qui vont déterminer la position de
chaque personnage sur le plateau. Leur position est connue à la création.
Les monstres sont cachés et n’apparaissent qu’une fois le combat commencé.
Le combat commencera automatiquement lorsque le héros se positionnera à côté, horizontalement
ou verticalement, d’un monstre.
Le Héro devra s’afficher par un H, les monstres s’afficheront avec un L pour loup, un O pour orque et
un D pour dragonnet.
Leu jeu s’arrête lorsqu’il n’y a plus de monstres sur la carte ou que le héros meurt.
'''
import random
from enum import Enum
class Character:
    def __init__(self):
        self.__stamina = self.generate_stamina_or_strength()
        self.__strength = self.generate_stamina_or_strength()
        self.__hp = self.generate_hp()
    
    def generate_stamina_or_strength(self) -> int:
        dice = random.randint(1,6)
        die_results = [dice]
        minimum = 0
        for i in range(3):
            dice = random.randint(1,6)
            if dice < die_results[minimum]:
                minimum = i + 1
            die_results.append(dice)
        die_results.pop(minimum)
        return sum(die_results)
    
    def generate_hp(self) -> int:
        if self.__stamina < 5:
            return self.__stamina - 1
        elif self.__stamina < 10:
            return self.__stamina
        elif self.__stamina < 15:
            return self.__stamina + 1
        else:
            return self.__stamina + 2
    
    def strike(self, target:Character) -> int:
        strike_damage = random.randint(1,4)
        if self.__strength < 5:
            strike_damage += self.__strength - 1
        elif self.__strength < 10:
            strike_damage += self.__strength
        elif self.__strength < 15:
            strike_damage += self.__strength + 1
        else:
            strike_damage += self.__strength + 2
        return strike_damage

    def heal(self, heal:int) -> None:
        self.__hp = heal

    def take_damage(self, damage:int) -> None:
        self.__hp -= damage

    @property
    def stamina(self):
        return self.__stamina
    @property
    def strength(self):
        return self.__strength
    @property
    def hp(self):
        return self.__hp

class Hero(Character):
    def __init__(self, name:str):
        super().__init__()
        self.__name = name
        self.__max_hp = self.hp
        self.__gold = 0
        self.__leather = 0
        self.__position = [0,0]

    def strike(self, target:Monster) -> bool:
        damage = super().strike(target)
        print(f"{self.__name} deals {damage} point(s) of damage to this {target.name} !")
        is_dead = target.take_damage(damage)
        if is_dead:
            target.get_looted(self)
            self.rest()
        return is_dead

    def take_damage(self, damage) -> bool:
        super().take_damage(damage)
        if self.hp <= 0:
            print(f"{self.name} died.")
            return True
        print(f"{self.name} has {self.hp} hp left.")
        return False
    
    def loot_golds(self, gold:int) -> None:
        self.__gold += gold

    def loot_leather(self, leather:int) -> None:
        self.__leather += leather
    
    def rest(self) -> None:
        super().heal(self.__max_hp)
        print(f"{self.name}, exhausted from his fight, rests and gets back to full life.")
    
    def change_pos(self, dir:list) -> None:
        self.__position[0] += dir[0]
        self.__position[1] += dir[1]

    @property
    def name(self):
        return self.__name
    @property
    def max_hp(self):
        return self.__max_hp
    @property
    def leather(self):
        return self.__leather
    @property
    def gold(self):
        return self.__gold
    @property
    def position(self):
        return self.__position

class Human(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__strength = self.strength + 1
        self.__stamina = self.stamina + 1

class Dwarf(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__stamina = self.stamina + 2

class Monster(Character):
    def take_damage(self, damage: int) -> bool:
        super().take_damage(damage)
        if self.hp <= 0:
            print(f"{self.name} died.")
            return True
        print(f"{self.name} has {self.hp} hp left.")
        return False
    
    def strike(self, target:Hero) -> bool:
        damage = super().strike(target)
        print(f"{self.name} deals {damage} point(s) of damage to {target.name} !")
        is_dead = target.take_damage(damage)
        return is_dead
    
    def get_looted(self):
        pass

    @property
    def name(self) -> str:
        return self.name

class Wolf(Monster):
    name = "Wolf"

    def __init__(self):
        super().__init__()
        self.__leather = random.randint(1,4)

    def get_looted(self, hero:Hero):
        hero.loot_leather(self.__leather)
        print(f"{hero.name} has looted {self.__leather} piece(s) of leather.")

class Orc(Monster):
    name = "Orc"

    def __init__(self):
        super().__init__()
        self.__strength = self.strength + 1
        self.__gold = random.randint(1,6)

    def get_looted(self, hero:Hero):
        hero.loot_golds(self.__gold)
        print(f"{hero.name} has looted {self.__gold} gold coin(s).")

class FledglingDragon(Monster):
    name = "Fledgling dragon"

    def __init__(self):
        super().__init__()
        self.__stamina = self.stamina + 1
        self.__gold = random.randint(1,6)
        self.__leather = random.randint(1,4)

    def get_looted(self, hero:Hero):
        hero.loot_leather(self.__leather)
        hero.loot_golds(self.__gold)
        print(f"{hero.name} has looted {self.__gold} gold coin(s) and {self.__leather} piece(s) of leather.")   

class Board():
    def __init__(self):
        self.__board = [["O"] * 15 for _ in range(15)]
        self.__real_board = [[None] * 15 for _ in range(15)]
        self.__population = 0
        self.__player_pos = [0,0]
    
    def display_board(self):
        for i in self.__board:
            print(i)
    
    def spawn_mobs(self):
        occupied_squares = [[0,0], [0,1],[1,0]]
        self.__board[0][0] = "H"
        for x in range(15):
            for y in range(15):
                spawn_chance = random.randint(0,4)
                if spawn_chance== 0 and [x,y] not in occupied_squares:
                    monster_pick = random.randint(1,3)
                    if monster_pick == 1:
                        self.__real_board[x][y] = Wolf()
                    elif monster_pick == 2:
                        self.__real_board[x][y] = Orc()
                    else:
                        self.__real_board[x][y] = FledglingDragon()
                    self.__population += 1
                    occupied_squares.append([x,y])
                    occupied_squares.append([x+1,y-1])
                    occupied_squares.append([x-1,y+1])

                    occupied_squares.append([x,y+1])
                    occupied_squares.append([x,y-1])
                    occupied_squares.append([x+1,y])
                    occupied_squares.append([x-1,y])
                    for i in range(0,3):
                        occupied_squares.append([x+i,y+(2-i)])
                        occupied_squares.append([x-(2-i), y-i])
                        occupied_squares.append([x+i,y-(2-i)])

    def update_player_position(self, player:Hero) -> None:
        self.__board[self.__player_pos[0]][self.__player_pos[1]] = "O"
        self.__real_board[self.__player_pos[0]][self.__player_pos[1]] = None
        self.__board[player.position[0]][player.position[1]] = "H"
        self.__real_board[player.position[0]][player.position[1]] = player
        self.__player_pos = player.position.copy()

    def move(self, player:Hero) -> None:
        direction = input("Where do you want to go ? (UP/DOWN/LEFT/RIGHT) : ")
        if player.position[0] + Direction[direction].value[0] < 0 or player.position[0] + Direction[direction].value[0] > 14 or player.position[1] + Direction[direction].value[1] < 0 or player.position[1] + Direction[direction].value[1] > 14:
            print("You are trying to run away from the battlefield, coward !")
            self.move(player)
        else:
            player.change_pos(Direction[direction].value)
            self.update_player_position(player)
            self.display_board()
    
    def play(self) -> None:
        player_name = input("What's your name adventurer ? : ")
        input_race = input("What do you want to play as ? (human/dwarf) : ")
        while input_race != "dwarf" and input_race != "human":
            input_race = input("This is not a valid race ! What do you want to play as ? (human/dwarf) : ")
        player = Human(player_name) if input_race == "human" else Dwarf(player_name)
        self.__real_board[0][0] = player
        self.spawn_mobs()
        self.display_board()
        while self.__population > 0 and player.hp > 0:
            print(f"There are {self.__population} enemies left !")
            self.move(player)
            enemy_position = self.find_enemy()
            if enemy_position:
                self.trigger_fight(player,enemy_position)
        if player.hp <= 0:
            print(f"Game Over ! During your adventures, you amassed {player.gold} gold coins and {player.leather} pieces of leather !")
        else:
            print(f"You won ! During your adventures, you amassed {player.gold} gold coins and {player.leather} pieces of leather !")
        
    def find_enemy(self) -> list:
        if self.__player_pos[0] > 0 and self.__real_board[self.__player_pos[0]-1][self.__player_pos[1]]:
            return [self.__player_pos[0]-1,self.__player_pos[1]]#self.__real_board[self.__player_pos[0]-1][self.__player_pos[1]]
        elif self.__player_pos[0] < 14 and self.__real_board[self.__player_pos[0]+1][self.__player_pos[1]]:
            return [self.__player_pos[0]+1,self.__player_pos[1]]#self.__real_board[self.__player_pos[0]+1][self.__player_pos[1]]
        elif self.__player_pos[1] > 0 and self.__real_board[self.__player_pos[0]][self.__player_pos[1]-1]:
            return [self.__player_pos[0],self.__player_pos[1]-1]#self.__real_board[self.__player_pos[0]][self.__player_pos[1]-1]
        elif self.__player_pos[1] < 14 and self.__real_board[self.__player_pos[0]][self.__player_pos[1]+1]:
            return [self.__player_pos[0],self.__player_pos[1]+1]#self.__real_board[self.__player_pos[0]][self.__player_pos[1]+1]
        
    def trigger_fight(self, player:Hero, monster_position:list):
        monster:Monster = self.__real_board[monster_position[0]][monster_position[1]]
        print(f"{player.name} is fighting a(n) {monster.name} !")
        is_combat_over = player.strike(monster)
        if is_combat_over:
            self.__real_board[monster_position[0]][monster_position[1]] = None
            self.__population -= 1
        else:
            is_combat_over = monster.strike(player)
        if not is_combat_over:
            player.strike(monster)

    @property
    def population(self) -> int:
        return self.__population

class Direction(Enum):
    UP = [-1,0]
    DOWN = [1,0]
    LEFT = [0,-1]
    RIGHT = [0,1]

board = Board()
board.play()