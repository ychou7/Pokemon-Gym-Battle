from abc import ABC, abstractmethod
from random import randint


# ABC stands for Abstract Base Classes
class Pokemon(ABC):

  def __init__(self, name, type):
    self._name = name
    self._type = type
    self._battle_table = [[1, 0.5, 2], [2, 1, 0.5], [0.5, 2, 1]]
    self._hp = 25

  @property
  def hp(self):
    return self._hp

  def get_normal_menu(self):
    return "Choose a Move:\n1. Slam\n2. Tackle\nEnter move: "

  move = 1
  move = 2

  def _normal_move(self, opponent, move):
    if move == 1:
      return self._slam(opponent)
    if move == 2:
      return self._tackle(opponent)

  def _slam(self, opponent):
    damage = randint(1, 8)
    opponent._take_damage(damage)
    return f"\n{self._name} SLAMS {opponent._name} for {damage} damage."

  def _tackle(self, opponent):
    damage = randint(3, 6)
    opponent._take_damage(damage)
    return f"\n{self._name} TACKLES {opponent._name} for {damage} damage."

  @abstractmethod
  def get_special_menu(self):
    pass

  @abstractmethod
  def _special_move(self, opponent, move):
    pass

  def attack(self, opponent, type, move):
    if type == 1:
      return self._normal_move(opponent, move)
    if type == 2:
      return self._special_move(opponent, move)

  def __str__(self):
    return f"{self._name} HP:{self._hp}/25"

  def _take_damage(self, dmg):
    self._hp = self._hp - dmg
    if self._hp < 0:
      self._hp = 0
