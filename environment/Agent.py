from environment.EnvObject import EnvObject


# Template for an agent which can interact with environments
class Agent(EnvObject):

    def __init__(self, size, field_of_view):
        self.field_of_view = field_of_view
        super().__init__(size)

    # Placeholder for a function that moves the agent based on input from the environment
    def move(self, *args):
        pass

    # Placeholder for a function that is called when the agent bumps into something
    def bumped(self):
        pass

    # Placeholder for a function that is called when the agent eats something
    def ate(self):
        pass

    # Returns the part of the screen's state corresponding to the field of view, centered on the agent
    def visible_part_of_screen(self, screen_state):
        center_x = self.get_pos()[0] + self.get_rect().width / 2
        center_y = self.get_pos()[1] + self.get_rect().height / 2
        left_x = int(center_x - self.field_of_view[0] / 2)
        right_x = int(center_x + self.field_of_view[0] / 2)
        top_y = int(center_y - self.field_of_view[1] / 2)
        bottom_y = int(center_y + self.field_of_view[1] / 2)
        return screen_state[left_x:right_x][top_y:bottom_y]

