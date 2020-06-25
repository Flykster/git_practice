#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Pokemon:
    
    experience_level_up = 10
    
    def __init__(self, name, level, strength, health, experience, max_health, is_knocked_out):
        self.name = name
        self.level = level
        self.type = strength
        self.current_health = health
        self.current_exp = experience
        self.max_health = max_health
        self.is_knocked_out = is_knocked_out
        
    def loose_health(self, total_points):
        self.current_health -= total_points
        print('''{name}'s health has reduced by {points} points. The current health is {current_health}.'''.format(name = self.name, points = total_points, current_health = self.current_health))
        
    
    def regain_health(self, total_point):
        self.current_health += total_points
        print('''{name}'s health has increased by {points} points. The current health is {current_health}.'''.format(name = self.name, points = total_points, current_health = self.current_health))
        
    
    def knock_out(self):
        if self.is_knocked_out == True:
            print('''{name} has been knocked out.'''.format(name = self.name))      
    
    def revive(self):
        print('''{name} is back in the game.'''.format(name = self.name))
        
    def attack(self, pokemon):
        damage = 0
        if self.is_knocked_out == False:
            
            if self.type == 'Fire' and pokemon.type == 'Grass':
                damage = 2*self.level
                self.current_exp += 1
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Fire' and pokemon.type == 'Water':
                damage = self.level/2
                self.current_exp += 1
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Fire' and pokemon.type == 'Fire':
                damage = 0
                self.current_exp += 0
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Water' and pokemon.type == 'Grass':
                damage = self.level/2
                self.current_exp += 1
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Water' and pokemon.type == 'Fire':
                damage = 2*self.level
                self.current_exp += 1
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Water' and pokemon.type == 'Water':
                damage = 0
                self.current_exp += 0
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Grass' and pokemon.type == 'Fire':
                damage = self.level/2
                self.current_exp += 1
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Grass' and pokemon.type == 'Water':
                damage = 2*self.level
                self.current_exp += 1
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
        
            elif self.type == 'Grass' and pokemon.type == 'Grass':
                damage = 0
                self.current_exp += 0
                pokemon.loose_health(damage)
                print('{attacking_pokemon} has attacked {attacked_pokemon}. Health of {attacked_pokemon} has reduced by {damage_points}.'.format(attacking_pokemon = self.name, attacked_pokemon = pokemon.name, damage_points = damage))
            
        else:
            print('''{name} cannot attack because it's knocked out.'''.format(name = self.name))
        
        if self.current_exp >= 10:
            self.level += 1
            print('''Kudos. {name} has now moved to the next level.'''.format(name = self.name))
        



class Trainer:
    
    potion_value = 100
    
    def __init__(self, name, pokemons, potion_number, currently_active_pokemon):
        self.trainer_name = name
        self.pokemon_list = pokemons
        self.potions = potion_number
        self.current_pokemon = currently_active_pokemon
    
    def attack_another_trainer(self, trainer):
        print('''{attacking_trainer} has attacked {attacked_trainer}. Their Pokemons will now fight.'''.format(attacking_trainer = self.trainer_name, attacked_trainer = trainer.trainer_name)+'\n')
        self.current_pokemon.attack(trainer.current_pokemon)

    
    def heal_pokemon(self):
        potions_available = self.potions
        if self.potions > 0:
            if self.current_pokemon.max_health <= 100:
                self.current_pokemon.regain_health(self.potion_value)
                potions_available -= 1
                print('You have successfully used 1 potion. You now have {potions} available with you.'.format(potions = potions_available))
            else:
                print('{name} is already at maximum health.'.format(name=self.current_pokemon.name))
        
        else:
            print('You do not have any potion to administer to your Pokemon.')
            
    def change_pokemon(self, pokemon_name):
        if pokemon_name in self.pokemon_list and pokemon_name.is_knocked_out == False:
            self.current_pokemon = pokemon_name
            print('Your current Pokemon is now {name}.'.format(name = pokemon_name))
         
        
        

#Playing game

pikachu = Pokemon("Pikachu", 3, "Fire", 100, 8, 100, False)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", 80, 8, 90, False)
squirtle = Pokemon("Squirtle", 3, "Water", 50, 5, 80, False)
charmander = Pokemon("Charmander", 3, "Fire", 40, 9, 100, False)


sagar = Trainer('Sagar', [pikachu], 2, pikachu)
piyush = Trainer('Piyush', [bulbasaur, squirtle], 2, bulbasaur)


        
pikachu.attack(bulbasaur)    
        
        
            
            
        
    


# In[ ]:




