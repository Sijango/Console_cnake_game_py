import ctypes
import os
import time

from scr.make_images_func import create_default_game_image, create_default_start_image, \
                                 create_default_pause_image, create_default_restart_image
from scr.food_logic import Food
from scr.status import KeyWindowStatus


class Window:
    def __init__(self):
        self.output_image = create_default_start_image()
        self.tmp_image = self.output_image
        self.window_key_status = KeyWindowStatus.ENTER
        self.x = 150
        self.y = 55
        self.data_start = 0

        self.food = Food()
        self.food.random_food()

        os.system(f'mode con cols={self.x} lines={self.y}')
        ctypes.windll.kernel32.SetConsoleTitleW('console_snake_game')

    def draw_image(self):
        for line_words in self.output_image:
            for word in line_words:
                print(word, end='')
            print('\n', end='')

    def update_image(self):
        if self.window_key_status != KeyWindowStatus.SPACE:
            self.output_image = create_default_game_image()
            self.output_image = self.food.draw_food(self.output_image)
        else:
            self.output_image = create_default_pause_image()

    def update_restart_image(self):
        self.output_image = create_default_restart_image()

    def update_food(self):
        self.food.random_food()

    def add_game_status(self, score: int = 0):
        self.output_image[2].append('   Счёт: ')
        self.output_image[2].append(f'{score}')
        time_now = time.perf_counter()
        self.output_image[4].append(f'   Игра идёт: {time_now - self.data_start:0.2f} секунд')

    def set_window_key_status(self, status):
        self.window_key_status = status

    def get_window_key_status(self):
        return self.window_key_status

    def get_image(self):
        return self.output_image

    def set_image(self, image):
        self.output_image = image

    def start_timer(self):
        self.data_start = time.perf_counter()


if __name__ == '__main__':
    wind = Window()
    wind.draw_image()

    input()
    wind.start_timer()
    os.system("cls")

    for i in range(15):
        wind.update_image()
        wind.add_game_status()
        wind.draw_image()
        time.sleep(1)
        os.system("cls")

    input()
