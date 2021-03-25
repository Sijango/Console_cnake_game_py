import os
import time

from scr.keyboard_logic import Keyboard
from scr.status import GameStatus, KeyWindowStatus
from scr.snake_logic import Snake
from scr.window_logic import Window


class Game:
    def __init__(self):
        self._snake = Snake()
        self._window = Window()
        self._keyboard = Keyboard()

        self._speed = 0.3
        self._max_speed = 0.04
        self._game_status = GameStatus.MENU_START

    def _work_main_window(self):
        self._window.draw_image()

        while True:
            self._window.set_window_key_status(self._keyboard.get_window_key())

            if self._window.get_window_key_status() == KeyWindowStatus.ENTER:
                self._game_status = GameStatus.GAME_START
                os.system('cls')
                break
            elif self._window.get_window_key_status() == KeyWindowStatus.ESC:
                time.sleep(3)
                self._game_status = GameStatus.MENU_EXIT
                self._work_out()
                break

    def _work_game(self):
        self._window.start_timer()

        while self._keyboard.get_window_key() != KeyWindowStatus.ESC:
            self._window.set_window_key_status(self._keyboard.get_window_key())

            if self._window.get_window_key_status() != KeyWindowStatus.SPACE:
                if self._snake.check_collision_with_border(self._window.get_image()) or \
                        self._snake.check_collision_with_itself(self._window.get_image()):
                    break

                if self._snake.check_collision_with_food(self._window.get_image()):
                    self._window.update_food()
                    self._snake.update_score()
                    self._snake.add_snake_segment()

                    if self._speed > 0.02:
                        self._speed -= 0.02

                self._snake.set_move_status(self._keyboard.get_snake_key())
                self._snake.change_of_coordinates()

                self._window.update_image()
                self._window.add_game_status(self._snake.get_score())

                image = self._window.get_image()
                self._window.set_image(self._snake.draw(image))

                self._window.draw_image()
                time.sleep(self._speed)
                os.system("cls")
            else:
                self._game_status = GameStatus.GAME_WAIT
                self._work_pause()

        if self._keyboard.get_window_key() != KeyWindowStatus.ESC:
            self._game_status = GameStatus.GAME_END
        else:
            time.sleep(3)
            self._game_status = GameStatus.MENU_EXIT
            self._work_out()

    def _work_pause(self):
        while True:
            if self._window.get_window_key_status() != KeyWindowStatus.SPACE:
                break

            self._window.update_image()
            self._window.draw_image()
            time.sleep(self._speed)
            os.system('cls')
            self._window.set_window_key_status(self._keyboard.get_window_key())

        if self._window.get_window_key_status() == KeyWindowStatus.ENTER:
            self._game_status = GameStatus.GAME_START
        else:
            self._game_status = GameStatus.MENU_EXIT
            self._work_out()

    def _work_out(self):
        self._keyboard.end_key_listener()
        time.sleep(1)

    def _work_restart(self):
        self._window.update_restart_image()
        self._window.draw_image()

        while True:
            self._window.set_window_key_status(self._keyboard.get_window_key())

            if self._window.get_window_key_status() == KeyWindowStatus.SPACE:
                self._snake = None
                self._snake = Snake()
                self._speed = 0.3
                self._window.update_food()
                self._game_status = GameStatus.GAME_START
                os.system('cls')
                break
            elif self._window.get_window_key_status() == KeyWindowStatus.ESC:
                time.sleep(3)
                self._game_status = GameStatus.MENU_EXIT
                self._work_out()
                break

    def start_the_game(self):
        self._keyboard.start_key_listener()
        self._work_main_window()

        while self._game_status != GameStatus.MENU_EXIT:
            print(self._keyboard.get_keyboard_status())
            if self._game_status == GameStatus.GAME_START:
                self._work_game()

            elif self._game_status == GameStatus.GAME_END:
                self._work_restart()


if __name__ == '__main__':
    game = Game()

    game.start_the_game()
