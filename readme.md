## Абстракция: 
 - Класс RobotBase является абстрактным классом, который определяет общую структуру и поведение для всех роботов. 
 - Метод move является абстрактным методом, который должен быть реализован в дочерних классах.

```py
# robot.py

from abc import ABC, abstractmethod


class RobotBase(ABC):
    """
    Абстрактный класс для робота.
    """

    def __init__(self, x, y):
        """
        Инициализация робота.

        :param x: координата x
        :param y: координата y
        """
        self.x = x
        self.y = y

    @abstractmethod
    def move(self, moves):
        """
        Абстрактный метод для перемещения робота.

        :param moves: список команд для перемещения
        """
        pass

```
## Наследование: 
- Класс Robot наследует от класса RobotBase и расширяет его функциональность. Он реализует абстрактный метод move и добавляет дополнительные методы и свойства.

```py
#robot.py

class Robot(RobotBase):
    """
    Класс для робота, который может перемещаться по координатам.
    """

    def __init__(self, x, y):
        """
        Инициализация робота.

        :param x: координата x
        :param y: координата y
        """
        if (0 <= x <= 100) and (0 <= y <= 100):
            super().__init__(x, y)
            self.path_cache = [(self.x, self.y)]
        else:
            raise ValueError("Робот должен располагаться в пределах диапазона")

    def move(self, moves):
        """
        Перемещение робота по командам.

        :param moves: список команд для перемещения
        :return: последняя координата робота
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
        
        # ...
```


## Инкапсуляция: 
- Класс Robot инкапсулирует данные и поведение робота. Он скрывает детали реализации и предоставляет публичные методы для взаимодействия с роботом.

## Полиморфизм: 
- Класс Robot может быть использован в любом месте, где ожидается объект класса RobotBase, поскольку он наследует от него и реализует его абстрактные методы.

```py
#main.py

from robot import Robot

if __name__ == "__main__":
    robot = Robot(0, 0)
    robot.move("WWWSSSNNNEEE")
    print(robot.path())
```