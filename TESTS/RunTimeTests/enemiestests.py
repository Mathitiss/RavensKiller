import unittest
from Game.LevelsHandler import LevelsHandler

class EnemiesTests(unittest.TestCase):
    
    def __init__(self, game):
        super().__init__()
        
        self.dr_group = game.deadly_raven_group
        self.fr_group = game.fly_raven_group
        self.gr_group = game.ground_raven_group
        
    
    def print_current_enemies(self):
        print(f"\nActive Deadly Ravens: {len(self.dr_group)}")
        print(f"Active Ground Ravens: {len(self.gr_group)}")
        print(f"Active Fly Ravens: {len(self.fr_group)}")

