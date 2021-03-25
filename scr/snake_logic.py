from scr.window_logic import Window
from scr.status import SnakeStatus, SnakeMove


class Snake:
    def __init__(self):
        self._snake_body = [['0', 46, 23], ['o', 47, 23], ['o', 48, 23], ['o', 49, 23]]
        self._score = 0
        self._segment = len(self._snake_body)
        self._snake_status = SnakeStatus.PAUSE
        self._snake_key = SnakeMove.LEFT

    def set_move_status(self, status):
        if self._snake_key == SnakeMove.LEFT and status != SnakeMove.RIGHT:
            self._snake_key = status

        elif self._snake_key == SnakeMove.RIGHT and status != SnakeMove.LEFT:
            self._snake_key = status

        elif self._snake_key == SnakeMove.UP and status != SnakeMove.DOWN:
            self._snake_key = status

        elif self._snake_key == SnakeMove.DOWN and status != SnakeMove.UP:
            self._snake_key = status

    def get_move_status(self):
        return self._snake_key

    def get_status(self):
        return self._snake_status

    def get_score(self):
        return self._score

    def update_score(self):
        self._score += 1

    def draw(self, image):
        for item in self._snake_body:
            segment = item[0]
            x = item[1]
            y = item[2]

            image[y][x] = segment

        return image

    def change_of_coordinates(self):
        temp = []

        for i, item in enumerate(self._snake_body):

            if i == 0:
                temp = item[1:3]

                if self._snake_key == SnakeMove.UP:
                    item[2] -= 1

                elif self._snake_key == SnakeMove.DOWN:
                    item[2] += 1

                elif self._snake_key == SnakeMove.LEFT:
                    item[1] -= 1

                elif self._snake_key == SnakeMove.RIGHT:
                    item[1] += 1

            else:
                temp, item[1:3] = item[1:3], temp

    def add_snake_segment(self):
        if self._snake_body[-1][1] == self._snake_body[-2][1]:

            if self._snake_body[-1][2] > self._snake_body[-2][2]:
                segment = self._snake_body[-1][0]
                x = self._snake_body[-1][1]
                y = self._snake_body[-1][2]

                self._snake_body.append([segment, x, y + 1])
            else:
                segment = self._snake_body[-1][0]
                x = self._snake_body[-1][1]
                y = self._snake_body[-1][2]

                self._snake_body.append([segment, x, y - 1])

        elif self._snake_body[-1][2] == self._snake_body[-2][2]:

            if self._snake_body[-1][1] > self._snake_body[-2][1]:
                segment = self._snake_body[-1][0]
                x = self._snake_body[-1][1]
                y = self._snake_body[-1][2]

                self._snake_body.append([segment, x + 1, y])
            else:
                segment = self._snake_body[-1][0]
                x = self._snake_body[-1][1]
                y = self._snake_body[-1][2]

                self._snake_body.append([segment, x - 1, y])

    def check_collision_with_border(self, image) -> bool:
        item = self._snake_body[0]

        if self._snake_key == SnakeMove.UP:
            x_snake = item[1]
            y_snake = item[2] - 1

        elif self._snake_key == SnakeMove.DOWN:
            x_snake = item[1]
            y_snake = item[2] + 1

        elif self._snake_key == SnakeMove.LEFT:
            x_snake = item[1] - 1
            y_snake = item[2]

        elif self._snake_key == SnakeMove.RIGHT:
            x_snake = item[1] + 1
            y_snake = item[2]

        segment_image = image[y_snake][x_snake]

        if segment_image == '#':
            return True

        return False

    def check_collision_with_itself(self, image) -> bool:
        item = self._snake_body[0]

        if self._snake_key == SnakeMove.UP:
            x_snake = item[1]
            y_snake = item[2] - 1

        elif self._snake_key == SnakeMove.DOWN:
            x_snake = item[1]
            y_snake = item[2] + 1

        elif self._snake_key == SnakeMove.LEFT:
            x_snake = item[1] - 1
            y_snake = item[2]

        elif self._snake_key == SnakeMove.RIGHT:
            x_snake = item[1] + 1
            y_snake = item[2]

        segment_image = image[y_snake][x_snake]

        if segment_image == 'o':
            return True

        return False

    def check_collision_with_food(self, image) -> bool:
        item = self._snake_body[0]

        if self._snake_key == SnakeMove.UP:
            x_snake = item[1]
            y_snake = item[2] - 1

        elif self._snake_key == SnakeMove.DOWN:
            x_snake = item[1]
            y_snake = item[2] + 1

        elif self._snake_key == SnakeMove.LEFT:
            x_snake = item[1] - 1
            y_snake = item[2]

        elif self._snake_key == SnakeMove.RIGHT:
            x_snake = item[1] + 1
            y_snake = item[2]

        segment_image = image[y_snake][x_snake]

        if segment_image == 'Q':
            return True

        return False


if __name__ == '__main__':
    snake = Snake()
    window = Window()
    snake.set_move_status(SnakeMove.UP)
    snake.change_of_coordinates()

    speed = 0.7

    if snake.check_collision_with_border(window.get_image()) or snake.check_collision_with_itself(window.get_image()):
        pass

    if snake.check_collision_with_food(window.get_image()):
        window.update_food()
        snake.update_score()

        if speed >= 0.2:
            speed -= 0.02

    print(snake._snake_body)
    snake.change_of_coordinates()

    print(snake._snake_body)
    snake.change_of_coordinates()

    print(snake._snake_body)
