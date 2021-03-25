import os
import time
import ctypes


def create_default_game_image(x: int = 100, y: int = 50):
    result_image = []

    for y_line in range(0, y):
        result_image.append([])

        for x_line in range(0, x):
            if y_line == 0 or x_line == 0 or y_line == 49 or x_line == 99:
                result_image[y_line].append('#')
            else:
                result_image[y_line].append(' ')

    return result_image


def create_default_start_image(x: int = 150, y: int = 50):
    result_image = []

    for y_line in range(0, y):
        result_image.append([])

        for x_line in range(0, x):
            if x_line == 40 and y_line == 23:
                result_image[y_line].append('Start game (press ENTER)')
            elif x_line == 40 and y_line == 24:
                result_image[y_line].append('Exit (press ESC)')
            else:
                result_image[y_line].append(' ')

    return result_image


def create_default_pause_image(x: int = 150, y: int = 50):
    result_image = []

    for y_line in range(0, y):
        result_image.append([])

        for x_line in range(0, x):
            if x_line == 40 or x_line == 110 or y_line == 15 or y_line == 35:
                result_image[y_line].append('#')
            elif x_line == 60 and y_line == 25:
                result_image[y_line].append('Для продолжения нажмите ENTER')
            else:
                result_image[y_line].append(' ')

    return result_image


def create_default_restart_image(x: int = 150, y: int = 50):
    result_image = []

    for y_line in range(0, y):
        result_image.append([])

        for x_line in range(0, x):
            if x_line == 40 and y_line == 23:
                result_image[y_line].append('Restart game (press SPACE)')
            elif x_line == 40 and y_line == 24:
                result_image[y_line].append('Exit (press ESC)')
            else:
                result_image[y_line].append(' ')

    return result_image


if __name__ == '__main__':
    DEFAULT_GAME_IMAGE = create_default_game_image()
    DEFAULT_START_IMAGE = create_default_start_image()
    DEFAULT_PAUSE_IMAGE = create_default_pause_image()

    os.system('mode con cols=150 lines=52')
    ctypes.windll.kernel32.SetConsoleTitleW('console_snake_game')

    for line_words in DEFAULT_PAUSE_IMAGE:
        print('\n', end='')
        for word in line_words:
            print(word, end='')

    time.sleep(5)
    os.system("cls")

    for line_words in DEFAULT_GAME_IMAGE:
        print('\n', end='')
        for word in line_words:
            print(word, end='')

    input()
else:
    DEFAULT_GAME_IMAGE = create_default_game_image()
    DEFAULT_START_IMAGE = create_default_start_image()
