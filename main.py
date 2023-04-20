from random import randint
from fire import Fire
from grass import Grass
from water import Water


def main():
  leader_type = randint(1, 3)
  if leader_type == 1:
    leader_pokemons = [Fire("Ninetales"), Fire("Arcanine"), Fire("Rapidash")]
  if leader_type == 2:
    leader_pokemons = [Water("Dewgong"), Water("Slowbro"), Water("Lapras")]
  if leader_type == 3:
    leader_pokemons = [
      Grass("Venusaur"),
      Grass("Exeggutor"),
      Grass("Victreebel")
    ]
  if leader_type == 1:
    str_leader_type = "FIRE"
  elif leader_type == 2:
    str_leader_type = "WATER"
  else:
    str_leader_type = "GRASS"
  print(
    f"PROF OAK:  Hello Trainer!\nToday you're off to fight your first gym battle of 1 vs. 3 {str_leader_type} pokemon.\nSelect the pokemon that you will fight with.\n1. I choose you, Charmander.\n2. Squirtle!  GO!\n3. We can do it, Bulbasaur!"
  )
  trainer_pokemon = int(input("Please choose a pokemon: "))
  if trainer_pokemon == 1:
    trainer_pokemon = Fire("Charmander")
  if trainer_pokemon == 2:
    trainer_pokemon = Water("Squirtle")
  if trainer_pokemon == 3:
    trainer_pokemon = Grass("Bulbasaur")

  print("--GYM BATTLE--")
  while leader_pokemons and trainer_pokemon._hp > 0:
    opponent = leader_pokemons[0]
    while True:
      print(f"GYM LEADER: I choose you:\n{opponent}\n{trainer_pokemon}")
      attack_type = int(input(
        "Choose an Attack Type:\n1. Normal\n2. Special\nEnter attack type: "))
      menu = trainer_pokemon.get_normal_menu() if attack_type == 1 else trainer_pokemon.get_special_menu()
      move = int(input(menu))
      print(trainer_pokemon.attack(opponent, attack_type, move))
      if opponent.hp == 0:
        print("GYM LEADER: NOOOOO! You defeated my pokemon!")
        leader_pokemons.pop(0)
        break
      leader_attack_type = randint(1, 2)
      leader_move = randint(1, 2)
      print(opponent.attack(trainer_pokemon, leader_attack_type, leader_move))
      if trainer_pokemon.hp == 0:
        print("GYM LEADER WON! The gym leader defeated you.")
        break
    if len(leader_pokemons) == 0:
      print("YOU WON! You defeated the gym leader.")


main()
