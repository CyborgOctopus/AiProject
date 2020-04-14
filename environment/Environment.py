import pickle
import pygame as pg

# Constants
BLACK = (0, 0, 0)


# Template for an environment with obstacles, food sources, and agents which try to collect food and avoid being eaten
class Environment:

    def __init__(self, screen_size, screen_color=BLACK):
        self.screen_size = screen_size
        self.screen_color = screen_color
        self.screen = self.create_screen()
        self.nutrients = pg.sprite.Group()
        self.obstacles = pg.sprite.Group()
        self.agents = pg.sprite.Group()
        self.create_obstacles()
        self.create_nutrients()
        pg.init()

    # Removes the screen attribute so that the environment can be pickled
    def __getstate__(self):
        self.__dict__.pop('screen')
        return self.__dict__

    # Restores the screen attribute during unpickling
    def __setstate__(self, state):
        self.__dict__ = state
        self.__dict__['screen'] = self.create_screen()

    # Function that runs the environment
    def run(self, display=True):
        while True:
            self.step(display)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

    # Function that advances the environment through a single time step
    def step(self, display=False):
        if display:
            self.wipe_and_redisplay()
        self.update()
        self.eat_nutrients()
        self.move_agents()

    # Placeholder for a function that updates the state of the environment
    def update(self):
        pass

    # Displays the nutrients, obstacles, and agents on the screen
    def display(self):
        self.nutrients.draw(self.screen)
        self.agents.draw(self.screen)
        self.obstacles.draw(self.screen)

    # Wipes everything from the screen and redisplays it
    def wipe_and_redisplay(self):
        pg.display.flip()
        self.screen.fill(self.screen_color)
        self.display()

    # Returns the screen image as a numpy array
    def get_state(self):
        return pg.surfarray.array2d(self.screen)

    # Gets the positions of the agents
    def get_agents_pos(self):
        return [agent.get_pos() for agent in self.agents.sprites()]

    # Sets the positions of the agents, making sure they can't pass through obstacles or off the screen.
    # Also ensures that prey are not treated as obstacles for predators.
    def move_agents(self):
        for i, agent in enumerate(self.agents.sprites()):
            agent.get_rect().clamp_ip(self.screen.get_rect())
            prev_pos = agent.get_pos()
            agent.move(self.get_state())
            for obstacle in pg.sprite.spritecollide(agent, self.obstacles, dokill=False):
                if agent is not obstacle and (agent in self.nutrients or obstacle not in self.nutrients):
                    agent.set_pos(prev_pos)
                    agent.bumped()

    # Placeholder for a function that creates obstacles in the environment
    def create_obstacles(self):
        pass

    # Placeholder for a function that creates nutrients in the environment
    def create_nutrients(self):
        pass

    # Placeholder for function that adds an agent to the environment. Should call add_agent_to_groups at some point.
    def add_agent(self, agent, prey=False):
        pass

    def add_agent_to_groups(self, agent, prey):
        self.agents.add(agent)
        self.obstacles.add(agent)
        if prey:
            self.nutrients.add(agent)

    # Allows agents to eat nutrients and removes eaten nutrients from the screen
    def eat_nutrients(self):
        for agent in self.agents.sprites():
            for nutrient in pg.sprite.spritecollide(agent, self.nutrients, dokill=False):
                if not (agent in self.nutrients.sprites() and nutrient in self.agents.sprites()):
                    nutrient.kill()
                    agent.ate()

    # Creates a screen on which the environment is displayed
    def create_screen(self):
        screen = pg.display.set_mode(self.screen_size)
        screen.fill(self.screen_color)
        return screen

    # Saves the environment to a specified file
    def save(self, filename):
        pickle.dump(self, open(filename + '.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    # Loads an environment from a specified file
    def load(filename):
        try:
            return pickle.load(open(filename + '.pkl', 'rb'))
        except FileNotFoundError:
            pass
