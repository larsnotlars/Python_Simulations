from IPython import display
import matplotlib.animation as animation
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)

fig = plt.figure()

lines = plt.plot([])
line = lines[0]
plt.xlim(0, 2*np.pi)
plt.ylim(-1.1, 1.1)


def animate(frame):
    y = np.sin(x + 2*np.pi * frame/100)
    line.set_data((x, y))


anim = animation.FuncAnimation(fig, animate, frames=100, interval=20)
writer = animation.writers['html']
video = anim.to_html5_video()
html = display.HTML(video)
display.display(html)

plt.close()
