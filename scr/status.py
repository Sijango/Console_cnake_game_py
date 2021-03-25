from enum import Enum


class GameStatus(Enum):   # Статусы окна игры
    MENU_START = 0  # Статус начального окна игры
    GAME_WAIT = 1   # Статус ожидания, когда игра на паузе
    GAME_START = 2  # Статус старта игры, когда игра идёт
    GAME_END = 3    # Статус окончания игры
    MENU_EXIT = 4   # Статус выхода из игры


class SnakeStatus(Enum):    # Статус змейки
    ALIVE = 0   # Змейка жива
    DEATH = 1   # Змейка мертва
    PAUSE = 2   # Змейка на паузе


class SnakeMove(Enum):      # Статус передвижения змейки
    UP = 0      # Движение вверх
    DOWN = 1    # Движение вниз
    LEFT = 2    # Движение влево
    RIGHT = 3   # Движение вправо


class KeyboardStatus(Enum):     # Статус работы клавиатуры
    ON = 0      # Включена
    OFF = 1     # Выключена


class KeyWindowStatus(Enum):       # Статус обработки клавиш
    SPACE = 0   # Нажата кнопка паузы (Space)
    ENTER = 1   # Нажата кнопка подтверждения (Enter)
    ESC = 2     # Нажата кнопка выхода из игры (Esc)


class FoodStatus(Enum):     # Статус еды
    GENERATE = 0    # Статус генерации еды
    CREATED = 1     # Статус существования еды
    EATEN = 2       # Статус съеденной еды
