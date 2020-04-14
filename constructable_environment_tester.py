import pygame as pg
from ConstructableEnvironment import ConstructableEnvironment
from UserControlledAgent import UserControlledAgent
from RandomAgent import RandomAgent

# Constants
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
agent_radius = 10
path = 'C:\\Users\\CyborgOctopus\\PycharmProjects\\AiProject'


# Runs an instance of ConstructableEnvironment in order to test it
def main():
    environment = ConstructableEnvironment((500, 500))
    environment.save(path + 'test')
    print("saved")

    # Create agents
    agent = UserControlledAgent((agent_radius * 2, agent_radius * 2))
    pg.draw.circle(agent.get_image(), BLUE, (agent_radius, agent_radius), agent_radius)
    agent1 = RandomAgent((agent_radius * 2, agent_radius * 2))
    pg.draw.circle(agent1.get_image(), GREEN, (agent_radius, agent_radius), agent_radius)

    # Single agent
    environment = ConstructableEnvironment.load(path + 'test')
    print("Place agent.")
    environment.add_agent(agent)
    print("Close to start predator-predator simulation")
    environment.run()

    # Predator-predator
    pg.display.quit()
    pg.time.delay(500)
    environment = ConstructableEnvironment.load(path + 'test')
    print("Place agents.")
    environment.add_agent(agent)
    environment.add_agent(agent1)
    print("Close to start predator-prey simulation")
    environment.run()

    # Predator-prey
    pg.display.quit()
    pg.time.delay(500)
    environment = ConstructableEnvironment.load(path + 'test')
    print("Place predator.")
    environment.add_agent(agent)
    print("Place prey.")
    environment.add_agent(agent1, prey=True)
    print("Close to start prey-prey simulation")
    environment.run()

    # Prey-prey
    pg.display.quit()
    pg.time.delay(500)
    environment = ConstructableEnvironment.load(path + 'test')
    print("Place agents.")
    environment.add_agent(agent, prey=True)
    environment.add_agent(agent1, prey=True)
    print("Close to exit simulations")
    environment.run()


if __name__ == '__main__':
    main()
