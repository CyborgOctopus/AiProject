import pygame as pg
from environment.EnvObject import EnvObject
from environment.Environment import Environment

# Constants
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
nutrient_radius = 5


# An environment which allows a user to graphically place obstacles, nutrients, and agents.
class ConstructableEnvironment(Environment):

    # Creates rectangular obstacles in the environment based on click-and-drag user input
    def create_obstacles(self):
        print("Place obstacles. Press Enter when done.")
        obstacle = pos_1 = pos_2 = None
        pg.init()
        while True:
            self.wipe_and_redisplay()
            if pos_1 is not None:
                pos_2 = pg.mouse.get_pos()
                obstacle = self.create_obstacle(pos_1, pos_2)
                self.screen.blit(obstacle.get_image(), obstacle.get_pos())
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos_1 = pg.mouse.get_pos()
                if event.type == pg.MOUSEBUTTONUP:
                    if pos_2 != pos_1:
                        self.obstacles.add(obstacle)
                    pos_1 = None
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    print("obstacles created")
                    return

    # Creates nutrients in the environment at the positions where the user clicks
    def create_nutrients(self):
        print("Place nutrients. Press Enter when done.")
        pg.init()
        while True:
            pg.display.flip()
            self.display()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    nutrient = EnvObject((nutrient_radius * 2, nutrient_radius * 2))
                    pg.draw.circle(nutrient.get_image(), GREEN, (nutrient_radius, nutrient_radius), nutrient_radius)
                    nutrient.set_pos(pg.mouse.get_pos())
                    self.nutrients.add(nutrient)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        print("nutrients created")
                        return

    # Adds an agent to the environment at the position where the user clicks
    def add_agent(self, agent, prey=False):
        pg.init()
        while True:
            pg.display.flip()
            self.display()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    agent.set_pos(pg.mouse.get_pos())
                    if pg.sprite.spritecollideany(agent, self.obstacles):
                        print("Cannot put agent inside obstacle.")
                        continue
                    self.add_agent_to_groups(agent, prey)
                    print("agent added")
                    return

    @staticmethod
    # Generates an obstacle based on two given points
    def create_obstacle(pos_1, pos_2):
        width = abs(pos_1[0] - pos_2[0])
        height = abs(pos_1[1] - pos_2[1])
        left = pos_1[0] if pos_1[0] < pos_2[0] else pos_2[0]
        top = pos_1[1] if pos_1[1] < pos_2[1] else pos_2[1]
        obstacle = EnvObject((width, height))
        obstacle.get_image().fill(WHITE)
        obstacle.set_pos((left, top))
        return obstacle
