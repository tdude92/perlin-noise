import pyglet
from noise import perlin_noise

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

height_map = perlin_noise(20, 20, sec_width = 25, sec_length = 25)

counter = 1
for row in range(len(height_map)):
    for point in range(len(height_map[row])):
        pt = height_map[row][point]
        batch.add(1, pyglet.gl.GL_POINTS, None, ("v2i", (point + 1, len(height_map[row]) - row)), ("c3B", (0, int(127 * (pt + 1)), 0)))
    print(counter)
    counter += 1
print("done")

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
