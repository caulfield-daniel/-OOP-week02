```py
# robot.py

class Robot:
    """
    Класс, представляющий робота,
    который может перемещаться по координатам x и y.
    """

    path_cache = []  # Список пройденных роботом точек

    def __init__(self, x, y):
        """
        Инициализирует робота с заданными координатами x и y.
        Если координаты находятся вне диапазона от 0 до 100,
        вызывает исключение ValueError.

        :param x: Координата x робота.
        :param y: Координата y робота.
        """
        if (0 <= x <= 100) and (0 <= y <= 100):
            self.x = x
            self.y = y
        else:
            raise ValueError("Координаты должны быть в пределах от 0 до 100!")

    def move(self, moves):
        """
        Перемещает робота в соответствии с заданными движениями.
        Движения задаются строкой, где
        "N" - север, "S" - юг,
        "W" - запад, "E" - восток.
        Если в строке присутствует неверный символ,
        вызывает исключение ValueError.

        :param moves: Строка, представляющая движения робота.
        :return: Координаты x и y робота после перемещения.
        """
        for m in moves:
            if (self.x > 100) or (self.y > 100):
                raise ValueError("Робот выходит за границы диапазона")
            if m == "N":
                self.y += 1
            elif m == "S":
                self.y -= 1
            elif m == "W":
                self.x -= 1
            elif m == "E":
                self.x += 1
            elif m == "":
                continue
            else:
                raise ValueError("Неверный символ!")

            self.path_cache.append((self.x, self.y))

        return self.path_cache[-1]

    def path(self):
        """
        Возвращает список координат, по которым перемещался робот.

        :return: Список координат.
        """
        return self.path_cache

```