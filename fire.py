from pokemon import Pokemon
from random import randint


# 0 fire
# 1 water
# 2 grass
class Fire(Pokemon):

  def __init__(self, name):
    super().__init__(name, 0)

  def get_special_menu(self):
    return "Choose a Move:\n1. Ember\n2. Fire Blast\nEnter move: "

  def _special_move(self, opponent, move):
    if move == 1:
      return self._ember(opponent)
    elif move == 2:
      return self._fire_blast(opponent)

  def _ember(self, opponent):
    damage = randint(1, 5)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)

    if multiplier == 2:
      effect = "\nIt was SUPER EFFECTIVE!\n"
    elif multiplier == .5:
      effect = "\nIt was not very effective.\n"
    else:
      effect = ""
    opponent._take_damage(total_damage)
    return f"\n{self._name} BURNS {opponent._name} with FIRE for {total_damage} damage.{effect}"

  def _fire_blast(self, opponent):
    damage = randint(3, 4)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    if multiplier == 2:
      effect = "\nIt was SUPER EFFECTIVE!\n"
    elif multiplier == .5:
      effect = "\nIt was not very effective.\n"
    else:
      effect = ""
    opponent._take_damage(total_damage)
    return f"\n{self._name} BLASTS {opponent._name} with FIRE for {total_damage} damage.{effect}"