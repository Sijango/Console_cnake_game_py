import os
import threading
import time

from pynput import keyboard

from scr.status import KeyWindowStatus, SnakeMove, KeyboardStatus
from scr.window_logic import Window
from scr.snake_logic import Snake


class Keyboard:
    def __init__(self):
        self._window_key = KeyWindowStatus.SPACE
        self._snake_key = SnakeMove.LEFT
        self._keyboard_status = KeyboardStatus.OFF
        self._thread = None

    def get_window_key(self):
        return self._window_key

    def get_snake_key(self):
        return self._snake_key

    def get_keyboard_status(self):
        return self._keyboard_status

    def _on_press(self, key):
        if key == keyboard.Key.up:
            self._snake_key = SnakeMove.UP
        elif key == keyboard.Key.down:
            self._snake_key = SnakeMove.DOWN
        elif key == keyboard.Key.left:
            self._snake_key = SnakeMove.LEFT
        elif key == keyboard.Key.right:
            self._snake_key = SnakeMove.RIGHT
        elif key == keyboard.Key.enter:
            self._window_key = KeyWindowStatus.ENTER
        elif key == keyboard.Key.space:
            self._window_key = KeyWindowStatus.SPACE
        elif key == keyboard.Key.esc:
            self._window_key = KeyWindowStatus.ESC

    def _on_release(self, key):
        print(key)
        if key == keyboard.Key.esc:
            self._keyboard_status = KeyboardStatus.OFF
            return False

    def _key_listener(self):
        with keyboard.Listener(
                on_press=self._on_press,
                on_release=self._on_release) as listener:
            listener.join()

    def start_key_listener(self):
        self._thread = threading.Thread(target=self._key_listener)
        self._thread.start()
        self._keyboard_status = KeyboardStatus.ON

    def end_key_listener(self):
        self._thread.join()


if __name__ == '__main__':
    snake = Snake()
    window = Window()
    key = Keyboard()

    key.start_key_listener()
    window.draw_image()

    input()

    window.start_timer()
    os.system('cls')

    while key.get_window_key() != KeyWindowStatus.ESC:
        speed = 0.3

        window.set_window_key_status(key.get_window_key())

        if window.get_window_key_status() != KeyWindowStatus.SPACE:
            if snake.check_collision_with_border(window.get_image()) or snake.check_collision_with_itself(window.get_image()):
                break

            if snake.check_collision_with_food(window.get_image()):
                window.update_food()
                snake.update_score()
                snake.add_snake_segment()

                if speed >= 0.02:
                    speed -= 0.02

            snake.set_move_status(key.get_snake_key())
            snake.change_of_coordinates()

            window.update_image()
            window.add_game_status(snake.get_score())

            image = window.get_image()
            window.set_image(snake.draw(image))

            window.draw_image()
            time.sleep(speed)
            os.system("cls")
        else:
            window.update_image()
            window.draw_image()
            time.sleep(speed)
            os.system('cls')
            window.set_window_key_status(key.get_window_key())

    key.end_key_listener()
    # snake.set_move_status(key.get_snake_key())
    # window.set_window_key_status(key.get_window_key())
    #
    # time.sleep(0.1)
    #
    # print(f'WINDOW: {window.get_window_key_status()}')
    # print(f'SNAKE: {snake.get_move_status()}')
