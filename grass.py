# 0 fire
# 1 water
# 2 grass
from pokemon import Pokemon
from random import randint


class Grass(Pokemon):

  def __init__(self, name):
    super().__init__(name, 2)

  def get_special_menu(self):
    return "Choose a Move:\n1. Razor Leaf\n2. Solar Beam\nEnter move: "

  def _special_move(self, opponent, move):
    if move == 1:
      return self._razor_leaf(opponent)
    if move == 2:
      return self._solar_beam(opponent)

  def _razor_leaf(self, opponent):
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
    return f"\n{self._name} RAZOR {opponent._name} with LEAVES for {total_damage} damage.{effect}"

  def _solar_beam(self, opponent):
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
    return f"\n{self._name} BEAMS {opponent._name} for {total_damage} damage.{effect}"
