import numpy as np
from environment.Agent import Agent
from NeuralNetwork import NeuralNetwork

# Parameters
num_extra_sensory_inputs = 0
num_actions = 5
greedy_choice_prob = 0.9
reward_for_nutrient_consumption = 1


# Agent controlled by a neural network which can be trained using reinforcement learning.
class NeuralAgent(Agent):

    def __init__(self, size, network_hidden_layer_sizes, field_of_view):
        self.has_bumped = False
        self.has_eaten = False
        self.sensory_inputs = []
        self.rewards = []
        self.actions = {0: (0, 0), 1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
        self.input_layer_size = num_extra_sensory_inputs + field_of_view[0] * field_of_view[1] + num_actions
        self.output_layer_size = 1
        self.brain = NeuralNetwork([self.input_layer_size] + network_hidden_layer_sizes + [self.output_layer_size])
        self.field_of_view = field_of_view
        super().__init__(size, field_of_view)

    # Trains the agent on a random sample of experiences through reinforcement learning
    def train(self, batch_size, discount_factor, learning_rate):
        batch_indices = np.random.choice(range(len(self.sensory_inputs) - 1), batch_size)
        batch_states = [self.sensory_inputs[i] for i in batch_indices]
        batch_new_states = [self.sensory_inputs[i + 1] for i in batch_indices]
        batch_rewards = [self.rewards[i + 1] for i in batch_indices]
        batch_targets = [reward + discount_factor * (max_q(new_state) - max_q(state))]
        training_inputs = self.brain.train_on_minibatch(self.sensory_inputs, self.rewards, learning_rate)

    # Determines how the agent should move using the neural network, based on data from the environment.
    # Resets all sensory input variables.
    def move(self, screen_state):
        sensory_input = self.visible_part_of_screen(screen_state).flatten()
        self.sensory_inputs.append(sensory_input)
        self.rewards.append(0)
        action = self.actions[np.random.randint(0, len(self.actions))]
        if np.random.uniform(0, 1) < greedy_choice_prob:
            action = self.find_best_action()
        pos = self.get_pos()
        self.set_pos((pos[0] + action[0], pos[1] + action[1]))
        self.has_bumped = False
        self.has_eaten = False

    # Allows 'has_bumped' to be set as 'True' if the agent runs into something
    def bumped(self):
        self.has_bumped = True

    # Allows 'has_eaten' to be set as 'True' if the agent eats something and gives a reward
    def ate(self):
        self.rewards[-1] += reward_for_nutrient_consumption
        self.has_eaten = True

    # Computes the q-value of a given

    # Returns the optimal action which the network could take
    def find_best_action(self):
        best_action_key = 0
        for key in range(len(self.actions)):
            if self.brain.run(self.sensory_inputs[-1] + [key]) \
                    > self.brain.run(self.sensory_inputs[-1] + [best_action_key]):
                best_action_key = key
        return self.actions[best_action_key]
