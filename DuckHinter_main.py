import random
import arcade
from math import pi, sin, cos, acos

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = arcade.color.CATALINA_BLUE
COOL_DOWN = 10
MAIN_STR = ""

def get_distance(obj1, obj2):
    return ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5

class Cross_hare:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cool_down = 0
        self.texturecrosshair = arcade.load_texture("img/crosshair.png")

    def draw(self):
       #arcade.draw_point(self.x, self.y, [0, 200, 200], 10)
        self.texturecrosshair.draw(self.x, self.y, 30, 30)
        if self.cool_down > 0:
            arcade.draw_point(self.x, self.y,[200, 0, 0], 20)

        # arcade.draw_text(str(self.get_degree()), self.x + 5, self.y + 5,[200, 0, 0], 14)

    def update(self):
        if self.cool_down > 0:
            self.cool_down -= 1

    def shoot(self):
        self.cool_down = COOL_DOWN

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def get_degree(self):
        dx = self.x - SCREEN_WIDTH / 2
        dy = self.y - 0
        r = (dx ** 2 + dy ** 2) ** 0.5
        return acos(dx / r) * 180 / pi



class Duck:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 50
        self.degrees = random.randint(45, 135)
        self.speed = 2
        self.dx = cos(self.degrees * pi / 180)
        self.dy = sin(self.degrees * pi / 180)
        self.texture = arcade.load_texture("img/duck.png")
        self.texture2 = arcade.load_texture("img/duck2.png")


    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self):
        if self.degrees >= 90 :
            self.texture.draw(self.x, self.y, 70, 70, self.degrees - 180,)
        else:
            self.texture2.draw(self.x, self.y, 70, 70, self.degrees)

    def is_out(self):
        return self.x < -10 or self.x > SCREEN_WIDTH + 10 or self.y > SCREEN_HEIGHT + 10

    def check_strike(self, cross):
        if cross.cool_down > 0:
            return get_distance(self, cross) < 30
        else:
            return False

        # arcade.draw_point(self.x, self.y, [200, 0, 0], 50)

class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(SCREEN_COLOR)
        self.step = 0
        self.lvl = 1
        self.score = 0
        self.set_mouse_visible(False)
        self.textureGrass = arcade.load_texture("img/grass.png")
        self.texturegun = arcade.load_texture("img/gun.png")
        self.texturegun2 = arcade.load_texture("img/gun2.png")
        self.duck_list = []

    def setup(self):
        # Настроить игру здесь
        # self.duck = Duck()
        self.cross_hare = Cross_hare()

    def get_info(self):
        st = "Киличество апдейтов: {}\n".format(self.step) + \
             "Счет: {}\n".format(self.score)
        return st

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()

        for duck in self.duck_list:
            duck.draw()

        arcade.draw_text(self.get_info(), 15, 500, arcade.color.WHITE)

        # arcade.draw_text(MAIN_STR, 300, 400, arcade.color.WHITE, 12, 500)
        # print(self.score)

        self.textureGrass.draw(400, 100, 900, 200)
        if self.cross_hare.get_degree() >= 90:
            self.texturegun.draw(400, -40, 500, 450, self.cross_hare.get_degree() + 232,)
        else:
            self.texturegun2.draw(400, -40, 500, 450, self.cross_hare.get_degree() - 45 )
        self.cross_hare.draw()

        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        self.step += 1
        self.cross_hare.update()
        if random.randint(1, 1000) < self.lvl + 5:
            self.duck_list.append(Duck())

        for duck in self.duck_list:
            duck.move()
            if duck.check_strike(self.cross_hare):
                self.duck_list.remove(duck)
                self.score += 1

            if duck.is_out():
                self.duck_list.remove(duck)
                self.score -= 1
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cross_hare.move_to(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.cross_hare.shoot()
        pass


    #def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()