import random

from scr.status import FoodStatus


class Food:
    def __init__(self):
        self._food = 'Q'
        self._x = 0
        self._y = 0
        self._food_status = FoodStatus.GENERATE

    def random_food(self):
        self._x = random.randrange(1, 98)
        self._y = random.randrange(1, 48)

    def get_status(self):
        return self._food_status

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def draw_food(self, image):
        image[self._y][self._x] = self._food
        self._food_status = FoodStatus.CREATED

        return image
