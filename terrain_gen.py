import pyglet
from noise import perlin_noise

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

height_map = perlin_noise(20, 20, sec_width = 25, sec_length = 25)
peak = 1
mountain = 0.8
grass = 0.45
sand = -0.2
water = -0.4
deep_water = -0.8

counter = 1
for row in range(len(height_map)):
    for point in range(len(height_map[row])):
        pt = height_map[row][point]
        if pt <= deep_water:
            batch.add(1, pyglet.gl.GL_POINTS, None, ("v2i", (point + 1, row + 1)), ("c3B", (17, 30, 108)))
        elif pt <= water:
            batch.add(1, pyglet.gl.GL_POINTS, None, ("v2i", (point + 1, row + 1)), ("c3B", (0, 96, 255)))
        elif pt <= sand:
            batch.add(1, pyglet.gl.GL_POINTS, None, ("v2i", (point + 1, row + 1)), ("c3B", (250, 218, 94)))
        elif pt <= grass:
            batch.add(1, pyglet.gl.GL_POINTS, None, ("v2i", (point + 1, row + 1)), ("c3B", (76, 187, 23)))
        elif pt <= mountain:
            batch.add(1, pyglet.gl.GL_POINTS, None, ("v2i", (point + 1, row + 1)), ("c3B", (169, 169, 169)))
        elif pt <= peak:
            batch.add(1, pyglet.gl.GL_POINTS, None, ("v2i", (point + 1, row + 1)), ("c3B", (255, 255, 255)))
    print(counter)
    counter += 1

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
