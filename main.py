from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enable = False
window.exit_button.enable = False


class Block(Button):
    def __init__(self, position=(0, 0, 0), texture='brick'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=1.0
        )


class Wall(Button):
    def __init__(self, position=(0, 0, 0), texture='brick', rotation_y=0):
        super().__init__(
            parent=scene,
            position=position,
            model='quad',
            origin_y=0.5,
            texture=texture,
            rotation_y=rotation_y,
            color=color.color(0, 0, random.uniform(0.1, 1.0)),
            scale=1.0
        )


for z in range(20):
    for x in range(20):
        voxel = Block(position=(x, 0, z))
    for y in range(5):
        wall_1 = Wall(position=(z, y, 19 + 0.5))
        wall_2 = Wall(position=(-0.5, y, z), rotation_y=-90)
        wall_3 = Wall(position=(z, y, -0.5), rotation_y=-180)
        wall_4 = Wall(position=(19.5, y, z), rotation_y=90)

# testing pycharm commit

player = FirstPersonController()

app.run()
