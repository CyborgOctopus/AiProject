from RandomEnvironment import RandomEnvironment
from NeuralAgent import NeuralAgent

# Training parameters
num_training_epochs = 1000
num_steps_per_epoch = 1000
discount_factor = 0.95
learning_rate = 1
hidden_layer_sizes = [30]

# Environment parameters
screen_size = (800, 800)
max_obs_size = (300, 300)
num_obstacles = 50
num_nutrients = 1000

# Other parameters
agent_size = 30
agent_fov = (100, 100)


# Trains an agent to navigate a randomly-generated environment
def main():
    env = RandomEnvironment(screen_size, max_obs_size, num_obstacles, num_nutrients)
    agent = NeuralAgent(agent_size, hidden_layer_sizes, agent_fov)
    for i in range(num_training_epochs):
        for j in range(num_steps_per_epoch):
            env.step()
