# 0 fire
# 1 water
# 2 grass
from pokemon import Pokemon
from random import randint


class Water(Pokemon):

  def __init__(self, name):
    super().__init__(name, 1)

  def get_special_menu(self):
    return "\nChoose a Move:\n1. Water Gun\n2. Bubble Beam\nEnter move: "

  def _special_move(self, opponent, move):
    if move == 1:
      return self._water_gun(opponent)
    if move == 2:
      return self._bubble_beam(opponent)

  def _water_gun(self, opponent):
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
    return f"\n{self._name} SHOTS {opponent._name} with WATER for {total_damage} damage.{effect}"

  def _bubble_beam(self, opponent):
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
