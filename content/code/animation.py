import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation

import numpy as np

t = np.arange(0., 10., 0.01)
f = np.sin(t)

NB_FRAMES = 200

smoothing_functions = [
                       lambda s: np.exp(-(s-NB_FRAMES)**2/(15.*NB_FRAMES))*len(t),
                       lambda s: len(t)/2. + \
                                 np.tan((s-NB_FRAMES/2.)*np.pi/(1.1*NB_FRAMES))*len(t)/
                                 (2.*np.tan(np.pi/2.2)),
                       lambda s: (10*np.sin((s-NB_FRAMES/2.)*4*np.pi/NB_FRAMES)**2 + s)*
                                 len(t)/(NB_FRAMES),
                       lambda s: 6.*len(t)/NB_FRAMES**3*(NB_FRAMES*s**2/2. - s**3/3.),
                       lambda s: np.sin(s*np.pi/2./NB_FRAMES)*len(t),
                       lambda s: len(t)*s/200,
                       lambda s, speed=5.: (np.arctan(-speed + s/200.*2.*speed) + \
                                            np.arctan(speed))*len(t)/(2.*np.arctan(speed))
                      ]

names = "exp tan sin^2+lin cube sin lin arctan".split()
                       


fig = plt.figure()
ax = plt.axes(xlim=(0,10), ylim=(-2, 2+len(smoothing_functions)))
lines = [ax.plot([], [], lw=2, label=name)[0] for name in names]

def animate(i):
    for k, phi in enumerate(smoothing_functions):
        line = lines[k]
        line.set_data(t[:int(phi(i))], f[:int(phi(i))] + k)
    return lines

anim = animation.FuncAnimation(fig, animate, frames=NB_FRAMES, interval=20, blit=True)
anim.save('test.m4v', fps=20, extra_args=['-vcodec', 'libx264'])
plt.legend()
plt.show()
