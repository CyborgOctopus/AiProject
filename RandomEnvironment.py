import random
import pygame as pg
from environment.EnvObject import EnvObject
from environment.Environment import Environment

# Constants
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
nutrient_radius = 5


# An environment with randomly sized and positioned (within specified bounds) obstacles and nutrients.
# The position of agents added to the environment is also randomly assigned.
class RandomEnvironment(Environment):

    def __init__(self, screen_size, max_obs_size, num_obstacles, num_nutrients):
        self.max_obs_size = max_obs_size
        self.num_obstacles = num_obstacles
        self.num_nutrients = num_nutrients
        super().__init__(screen_size)

    # Creates randomly sized and positioned rectangular obstacles in the environment
    def create_obstacles(self):
        for i in range(self.num_obstacles):
            pos = (random.randrange(self.screen_size[0]), random.randrange(self.screen_size[1]))
            size = (random.randrange(1, self.max_obs_size[0]), random.randrange(1, self.max_obs_size[1]))
            obstacle = EnvObject(size)
            obstacle.get_image().fill(WHITE)
            obstacle.set_pos(pos)
            self.obstacles.add(obstacle)

    # Creates randomly positioned food particles in the environment
    def create_nutrients(self):
        for i in range(self.num_nutrients):
            pos = (random.randrange(self.screen_size[0]), random.randrange(self.screen_size[1]))
            nutrient = EnvObject((nutrient_radius * 2, nutrient_radius * 2))
            pg.draw.circle(nutrient.get_image(), GREEN, (nutrient_radius, nutrient_radius), nutrient_radius)
            nutrient.set_pos(pos)
            self.nutrients.add(nutrient)

    # Adds an agent to the environment at a random position
    def add_agent(self, agent, prey=False):
        while True:
            agent.set_pos((random.randrange(self.screen_size[0]), random.randrange(self.screen_size[1])))
            if not pg.sprite.spritecollideany(agent, self.obstacles):
                break
        self.add_agent_to_groups(agent, prey)
