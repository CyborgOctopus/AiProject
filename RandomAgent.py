import random
from environment.Agent import Agent


class RandomAgent(Agent):

    def move(self, *args):
        delta_x = random.randint(-1, 1)
        delta_y = random.randint(-1, 1)
        self.set_pos((self.get_pos()[0] + delta_x, self.get_pos()[1] + delta_y))