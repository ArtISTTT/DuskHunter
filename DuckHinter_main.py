import random
import arcade
from math import pi, sin, cos

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = arcade.color.CATALINA_BLUE

class Duck:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 50
        self.degrees = random.randint(30, 150)
        self.speed = 2
        self.dx = cos(self.degrees * pi / 180)
        self.dy = sin(self.degrees * pi / 180)
        self.texture = arcade.load_texture("img/duck.jpg")

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self):
        self.texture.draw(self.x, self.y, 30, 30)
        # arcade.draw_point(self.x, self.y, [200, 0, 0], 50)

class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(SCREEN_COLOR)

    def setup(self):
        # Настроить игру здесь
        self.duck = Duck()
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.duck.draw()
        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        self.duck.move()
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
