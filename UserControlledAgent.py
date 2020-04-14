import pygame as pg
import keyboard
from environment.Agent import Agent


# Agent which can be controlled by user input
class UserControlledAgent(Agent):

    # Allows the agent to move around its environment based on keyboard input
    def move(self, *args):
        pg.time.delay(10)
        delta_x = 0
        delta_y = 0
        if keyboard.is_pressed('left'):
            delta_x = -1
        if keyboard.is_pressed('right'):
            delta_x = 1
        if keyboard.is_pressed('down'):
            delta_y = 1
        if keyboard.is_pressed('up'):
            delta_y = -1
        self.set_pos((self.get_pos()[0] + delta_x, self.get_pos()[1] + delta_y))
