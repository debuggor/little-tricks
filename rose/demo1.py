# -*- coding:utf-8 -*-

import numpy as np
from mayavi import mlab

#玫瑰花的花朵
[x, t] = np.meshgrid(np.array(range(25))/24.0, np.arange(0, 575.5, 0.5)/575*17*np.pi-2*np.pi)
p = (np.pi/2)*np.exp(-t/(8*np.pi))
u = 1-(1-np.mod(3.6*t, 2*np.pi)/np.pi)**4/2
y = 2*(x**2-x)**2*np.sin(p)
r = u*(x*np.sin(p)+y*np.cos(p))
mlab.mesh(r*np.cos(t), r*np.sin(t), u*(x*np.cos(p)-y*np.sin(p)))

#玫瑰花的花杆
x1 = np.linspace(-0.1,0,200)
y1 = np.linspace(-0.1,0,200)
z1 = np.linspace(-4,0.0,200)
mlab.plot3d(x1,y1,z1,colormap='copper',representation='wireframe')

mlab.show()
