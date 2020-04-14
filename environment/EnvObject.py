import pygame as pg


# A class for objects in the environment
class EnvObject(pg.sprite.Sprite):
    
    def __init__(self, size):
        super().__init__()
        self.image = self.create_image(size)
        self.rect = self.image_rect()

    # Changes the image attribute to a string so that it can be pickled
    def __getstate__(self):
        self.image = pg.image.tostring(self.image, 'RGB'), self.image.get_size()
        return self.__dict__

    # Restores the image attribute from a string to a pygame surface
    # Known issue: If the image had size zero, attempted restoration will result in an exception
    def __setstate__(self, state):
        self.__dict__ = state
        image_string, size = self.image
        self.image = pg.image.fromstring(image_string, size, 'RGB')

    # Gets the surface containing the object image
    def get_image(self):
        return self.image

    # Gets the object rect
    def get_rect(self):
        return self.rect

    # Gets the position of the object
    def get_pos(self):
        return self.rect.x, self.rect.y

    # Sets the position of the object
    def set_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    # Creates a Surface on which the image of the object will be displayed
    @staticmethod
    def create_image(size):
        return pg.Surface(size)

    # Generates a rect for the object
    def image_rect(self):
        return self.image.get_rect()
