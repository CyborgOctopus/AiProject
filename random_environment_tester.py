import pygame as pg
from RandomEnvironment import RandomEnvironment
from UserControlledAgent import UserControlledAgent
from RandomAgent import RandomAgent

# Constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
agent_radius = 10


# Runs an instance of RandomEnvironment with a user-controlled agent in order to test it
def main():

    # Create environment and add user-controlled agent
    screen_size, max_obs_size, num_obstacles, num_nutrients, num_predators = get_user_input()
    environment = RandomEnvironment(screen_size, max_obs_size, num_obstacles, num_nutrients)
    agent = UserControlledAgent((agent_radius * 2, agent_radius * 2))
    pg.draw.circle(agent.get_image(), BLUE, (agent_radius, agent_radius), agent_radius)
    environment.add_agent(agent, prey=True)

    # Add random predators
    for i in range(num_predators):
        random_predator = RandomAgent((agent_radius * 2, agent_radius * 2))
        pg.draw.circle(random_predator.get_image(), RED, (agent_radius, agent_radius), agent_radius)
        environment.add_agent(random_predator)

    environment.run()


# Gets user input for the screen size, max obstacle size, number of obstacles, number of nutrients, and number of random
# predators in the environment
def get_user_input():
    return (int(input("Screen width: ")), int(input("Screen height: "))), \
           (int(input("Max obstacle width: ")), int(input("Max obstacle height: "))), \
           int(input("Number of obstacles: ")), \
           int(input("Number of nutrients: ")), \
           int(input("Number of predators: "))


if __name__ == '__main__':
    main()
