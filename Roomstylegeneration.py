import random

class weapon:
    # WEAPONS:
    # Name                |Damage|
    # Starter Sword       | 1    |
    # Adventurer's Sword  | 2-3  |
    # Knight's Sword      | 4-7  |
    # Guard's Sword       | 8-10 |
    # Serpants Sword      | 11-15|
    # Kebab               | >=16 |



    def __init__(self,level_num):
        self.drawing = "W"
        if level_num == 0:
            self.weapon_name = "Starter Sword"
            self.weapon_damage = 1
        else:
            self.weapon_damage = random.randint(level_num + 1, level_num * 2)
            if self.weapon_damage < 4:
                self.weapon_name = "Adventurer's Sword"
            elif self.weapon_damage < 8:
                self.weapon_name = "Knight's Sword"
            elif self.weapon_damage < 11:
                self.weapon_name = "Guard's Sword"
            elif self.weapon_damage < 16:
                self.weapon_name = "Serpant's Sword"
            else:
                self.weapon_name = "Kebab" #Change this lol


class potion:
    # POTIONS:
    # Name             | ID | Effect
    # Health Potion    | 1  | Heals.
    # Attack Potion    | 2  | Boosts Attack by 2-3x multiplier for 1 battle
    # Defense Potion   | 3  | Boosts Defense by 2-3x multiplier for 1 battle
    # Health Potion +  | 1  | Base Health +1
    # Attack Potion +  | 2  | Base Attack +1
    # Defense Potion + | 3  | Base Defense +1
    def __init__(self,level_num):

        self.drawing = "P"
        self.potion_effect = 0
        if random.randint(0,4) == 0:
            self.potion_type = random.randint(4,6)
            if self.potion_type == 4:
                self.potion_name = "Health Potion +"
            elif self.potion_type == 5:
                self.potion_name = "Attack Potion +"
            elif self.potion_type == 6:
                self.potion_name = "Defense Potion +"
        else:
            self.potion_type = random.randint(1,3)
            if self.potion_type == 1:
                self.potion_name = "Health Potion"
                self.potion_effect = random.randint(int(level_num/2) + 1, level_num * 2)
            elif self.potion_type == 2:
                self.potion_name = "Attack Potion"
                self.potion_effect = random.randint(2,3)
            elif self.potion_type == 3:
                self.potion_name = "Defense Potion"
                self.potion_effect = random.randint(2,3)


class gold:
    def __init__(self,level_num):
        self.drawing = "G"
        if level_num == 0:
            self.gold_amount = 1
        else:
            self.gold_amount = random.randint(level_num, level_num*3)


class player:
    def __init__(self,x,y,room_x,room_y):
        self.player_x, self.player_y = x,y
        self.player_room_x, self.player_room_y = room_x, room_y
        self.player_max_hp = 5
        self.player_hp = 5
        self.player_max_inv = 3
        self.player_inv = []
        self.player_weapon = weapon(0) # (weapons autopick up when stepped on, if the weapon on ground is higher damage)(will swap with weapon on ground)
        self.player_base_attack = 1
        self.player_gold = 0
        self.player_base_defense = 1
        self.player_attack_multiplier = 1
        self.player_defense_multiplier = 1
        
    def player_attack(self):
        attack_damage = (self.player_base_attack + self.player_weapon.weapon_damage) * self.player_attack_multiplier
        if random.randint(0,9) == 0:
            attack_damage *= 3
        return attack_damage
    def damage_player(self,enemy_attack):
        damage_dealt = enemy_attack - (self.player_base_defense * self.player_defense_multiplier)
        if damage_dealt > 0:
            self.player_hp -= damage_dealt
        player_death_flag = False
        if self.player_hp <= 0:
            player_death_flag = True
        return damage_dealt, player_death_flag
    def move(self,direction,floor_map,object_map):
        if direction == "n":
            if self.player_y == 0:
                if floor_map[self.player_y][self.player_x] == "D":
                    self.player_room_y -= 1
                    self.player_y = 9
                else:
                    return "wall"
            elif object_map[self.player_y-1][self.player_x] != " ":
                return object_map[self.player_y-1][self.player_x].drawing
            else:
                self.player_y -= 1
                return "moved"
       
        elif direction == "e":
            if self.player_x == 9:
                if floor_map[self.player_y][self.player_x] == "D":
                    self.player_room_x += 1
                    self.player_y = 9
                else:
                    return "wall"
            elif object_map[self.player_y][self.player_x+1] != " ":
                return object_map[self.player_y][self.player_x+1].drawing
            else:
                self.player_x += 1
                return "moved"
        
        elif direction == "s":
            if self.player_y == 9:
                if floor_map[self.player_y][self.player_x] == "D":
                    self.player_room_y -= 1
                    self.player_y = 0
                else:
                    return "wall"
            elif object_map[self.player_y+1][self.player_x] != " ":
                return object_map[self.player_y+1][self.player_x].drawing
            else:
                self.player_y += 1
                return "moved"
        
        elif direction == "w":
            if self.player_x == 0:
                if floor_map[self.player_y][self.player_x] == "D":
                    self.player_room_x -= 1
                    self.player_y = 0
                else:
                    return "wall"
            elif object_map[self.player_y][self.player_x+1] != " ":
                return object_map[self.player_y][self.player_x+1].drawing
            else:
                self.player_x -= 1
                return "moved"
    

class enemy:
    def __init__(self,level_dif,level_num):
        self.enemy_type = random.randint(0,2) #Ignore for now:
        self.enemy_name = "Jun"
        self.enemy_hp = random.randint(int(level_dif/2)+1,level_dif + 3)
        self.enemy_damage = random.randint((int(level_dif/2)+1),level_dif)
        self.drawing = "E"
        if random.randint(0,2) == 0:
            self.enemy_loot = [weapon(level_num),potion(level_num), gold(level_num)][random.randint(0,2)]
        else:
            self.enemy_loot = gold(0)
    def attack_enemy(self):
        pass
    def damage_enemy(self,player_attack):
        self.enemy_hp -= player_attack
        enemy_death_flag = False
        if self.enemy_hp <= 0:
            enemy_death_flag = True
        return player_attack, enemy_death_flag


class chest:
    def __init__(self,level_num): 
        self.chest_item = [weapon(level_num), potion(level_num), gold(level_num)][random.randint(0,2)]
        self.drawing = "C"


class room:
    # Types of Rooms                                                | room_type (string)
    # 1. Spawn Room: Add player/Spawn point, no enemies             | spawn
    # 2. Exit Room: Has staircase, random chance of boss/loot       | exit
    # 3. Body Room: Can have enemies, chests, keys, etc             | body
    # 4. Shop Room: Buy items on pedestals                          | shop
    # 5. Empty Room: Has no connections to it                       | empty
    
    # Floor map Key:
    # D = Door to another room
    # S = Spawnpoint
    # E = Exit
    #Objects
    # C = Chest
    # P = Player
    # E = Enemy

    # floor_map : information for each tile, such as exits, spawn point, generally rendered on bottom, then ontop objects are rendered
    # objects: information ontop of each tile, such as player, and enemies, each come with x,y cords
    def __init__(self): # Blank Room generation on init
        self.floor_map = []
        for i in range(10):
            self.floor_map.append([])
            for i2 in range(10):
                self.floor_map[i].append(" ")
        self.object_map = []
        for i in range(10):
            self.object_map.append([])
            for i2 in range(10):
                self.object_map[i].append(" ")
        
        self.branches = []
        self.room_type = "empty"
       

    def gen_spawnpoint(self):
        spawnpoint = random.randint(0,3)
        self.room_type = "spawn"
        if spawnpoint == 0:
            self.floor_map[4][4] = "S"
        elif spawnpoint == 1:
            self.floor_map[4][5] = "S"
        elif spawnpoint == 2:
            self.floor_map[5][4] = "S"
        elif spawnpoint == 3:
            self.floor_map[5][5] = "S"
        
    def gen_exit(self):
        exitpoint = random.randint(0,3)
        self.room_type = "exit"
        if exitpoint == 0:
            self.floor_map[4][4] = "0"
        elif exitpoint == 1:
            self.floor_map[4][5] = "0"
        elif exitpoint == 2:
            self.floor_map[5][4] = "0"
        elif exitpoint == 3:
            self.floor_map[5][5] = "0"
    
    # Places doors on floor_map
    def gen_paths(self): #brances : tuple/list of directions ("n","e","s","w") (lowercase)
        for l in self.branches:
            if l == "n":
                self.floor_map[0][4],self.floor_map[0][5] = "D","D"
            elif l == "e":
                self.floor_map[4][9],self.floor_map[5][9] = "D","D"
            elif l == "s":
                self.floor_map[9][4],self.floor_map[9][5] = "D","D"
            elif l == "w":
                self.floor_map[4][0],self.floor_map[5][0] = "D","D"
    
    #Fills room based on type
    def fill_room(self,level_num,level_difficulty):
        if self.room_type == "spawn":
            if random.randint(0,4) == 0:
                self.object_map[0][9] = chest(level_num)
            elif random.randint(0,19) == 0:  # CHANGE ODDS LATER
                self.object_map[0][0] = chest(level_num + 2)
        elif self.room_type == "body":
            enemy_count = 0
            spawn_chest = False
            if random.randint(0,1) == 0:
                enemy_count = random.randint(1,3)
            if random.randint(0,2) == 0:
                spawn_chest = True
            if enemy_count == 0 and spawn_chest == 0:
                if random.randint(0,1) == 1:
                    enemy_count = 1
                else:
                    spawn_chest = True

            if spawn_chest:
                if random.randint(1,2) == 1:
                    self.object_map[0][0] = chest(level_num)
                else:
                    self.object_map[0][9] = chest(level_num)
                    
            while enemy_count > 0:
                enemy_spawn_x, enemy_spawn_y = random.randint(1,8), random.randint(1,8)
                if self.object_map[enemy_spawn_x][enemy_spawn_y] == " ":
                    enemy_count -= 1
                    self.object_map[enemy_spawn_x][enemy_spawn_y] = enemy(level_difficulty,level_num)   
        elif self.room_type == "exit":
            pass

#Creates path from a point to another point, shortest path, slightly random.
def pathfind(x1,y1,x2,y2):
    x_dif = x1 - x2
    y_dif = y1 - y2
    path = []
    while x_dif != 0 or y_dif != 0:      
        if x_dif !=0 and y_dif != 0:
            if random.randint(0,1) == 0:
                if x_dif > 0:
                    path.append("w")
                    x_dif -= 1
                elif x_dif < 0:
                    path.append("e")
                    x_dif += 1
            else:
                if y_dif > 0:
                    path.append("n")
                    y_dif -= 1
                elif y_dif < 0:
                    path.append("s")
                    y_dif += 1
        
        #Straight Paths
        elif y_dif != 0:
            if y_dif > 0:
                while y_dif > 0:
                    path.append("n")
                    y_dif -= 1
                return path
            elif y_dif < 0:
                while y_dif < 0:
                    path.append("s")
                    y_dif += 1
                return path
        elif x_dif != 0:
            if x_dif > 0:
                while x_dif > 0:
                    path.append("w")
                    x_dif -= 1
                return path
            elif x_dif < 0:
                while x_dif < 0:
                    path.append("e")
                    x_dif += 1
                return path
    return path


class level:
    #Levels are made up of rooms, and the level class calls the functions for generating rooms, blank room is created on init
    # 7x7 Array max
    # First generates blank 7x7 array of rooms, then decides which paths to create.
    def __init__(self,level_num,difficulty,size): # Generates Blank size x size array with blank rooms (probably 7x7)
        self.level_difficulty = level_num * difficulty
        self.level_num = level_num
        self.level_data = []
        self.size = size
        for i in range(size):
            self.level_data.append([])
            for i2 in range(size):
                self.level_data[i].append(room())
    
    def branch(self,branch_dirs,x,y):
        if branch_dirs == "spawn":
            self.level_data[y][x].branches = ["n","e","s","w"]
            self.level_data[y-1][x].branches.append("s")
            self.level_data[y-1][x].room_type = "body"
            self.level_data[y+1][x].branches.append("n")
            self.level_data[y+1][x].room_type = "body"
            self.level_data[y][x-1].branches.append("e")
            self.level_data[y][x-1].room_type = "body"
            self.level_data[y][x+1].branches.append("w")
            self.level_data[y][x+1].room_type = "body"
        else:
            for d in branch_dirs:   
                if d == "n":
                    self.level_data[y][x].branches.append("n")
                    self.level_data[y-1][x].branches.append("s")
                elif d == "e":
                    self.level_data[y][x].branches.append("e")
                    self.level_data[y][x+1].branches.append("w")
                elif d == "s":
                    self.level_data[y][x].branches.append("s")
                    self.level_data[y+1][x].branches.append("n")
                elif d == "w":
                    self.level_data[y][x].branches.append("w")
                    self.level_data[y][x-1].branches.append("e")
    
    def fill_doors(self):
        for l in range(self.size):
            for l2 in range(self.size):
                self.level_data[l][l2].gen_paths()
    def fill_all_rooms(self):
        for layer in self.level_data:
            for room in layer:
                room.fill_room(self.level_num,self.level_difficulty)
    def gen_level_map(self):
        #Spawn Room generation
        spawn_room_x, spawn_room_y = random.randint(1, self.size-2),random.randint(1, self.size-2) #Generates spawn room (never will touch border)
        self.branch("spawn", spawn_room_x, spawn_room_y)
        self.level_data[spawn_room_y][spawn_room_x].gen_spawnpoint()
        
        # Exit Room generation
        exit_room_x, exit_room_y = random.randint(0,self.size-1),random.randint(0,self.size-1)
        while (exit_room_x == spawn_room_x and exit_room_y == spawn_room_y):
            exit_room_x, exit_room_y = random.randint(0,self.size-1),random.randint(0,self.size-1)
        self.level_data[exit_room_y][exit_room_x].gen_exit()

        #Body Room generation:
        # Steps:
        # Generate Path towards exit
        # Branch between each of those room
        fill_cords = [spawn_room_x,spawn_room_y]
        spawn_exit = pathfind(spawn_room_x,spawn_room_y,exit_room_x,exit_room_y)
        for l in spawn_exit:
            self.branch([l],fill_cords[0],fill_cords[1])
            if l == "n":
                fill_cords[1] -= 1
            elif l == "s":
                fill_cords[1] += 1
            elif l == "e":
                fill_cords[0] += 1
            elif l == "w":
                fill_cords[0] -= 1
            if self.level_data[fill_cords[1]][fill_cords[0]].room_type == "empty":
                self.level_data[fill_cords[1]][fill_cords[0]].room_type = "body"
        
        





    def gen_all(self):
        self.gen_level_map()
        self.fill_doors()
        self.fill_all_rooms()
        

def draw_current_room(level,player_room_x,player_room_y,player_x,player_y):
    floor = level.level_data[player_room_y][player_room_x].floor_map
    objects = level.level_data[player_room_y][player_room_x].object_map
    for f in range(len(floor)):
        print_layer = ""
        for f2 in range(len(floor)):
            if player_y == f and player_x == f2:
                print_layer += "[P]"
            elif floor[f][f2] == " " and objects[f][f2] == " ":
                print_layer += "[ ]"
            elif floor[f][f2] != " " and objects[f][f2] == " ":
                print_layer += "[" + floor[f][f2] + "]"
            elif floor[f][f2] == " " and objects[f][f2] != " ":
                print_layer += "[" + objects[f][f2].drawing + "]"
            elif floor[f][f2] != " " and objects [f][f2] != " ":
                print_layer += "[" + objects[f][f2].drawing + "]"
                
        print(print_layer)
    


# messing around code below

main = True

while main:
    break


level1 = level(1,1,3)
level1.gen_all()


for i in range(level1.size):
    for i2 in range(level1.size):
        draw_current_room(level1,i2,i,0,9)
        print("______________________________")


print("end")