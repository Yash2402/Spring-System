import pygame
from lib.spring import Point, Spring
from lib.vector2d import Vector2D
import numpy as np

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w = 10
# 1580 950
n = 2500
nprow = 100
rows = int(n/nprow)
x = 100
y = 100

points = np.empty([nprow, rows], dtype=Point)
for i in range(nprow):
    for j in range(rows):
        points[i][j] = Point(x+i*w, y+j*w, (i, j))

for c in range(nprow):
    points[c][0].lock()
    # points[c][rows-1].lock()
# for a in range(rows):
    # points[0][a].lock()
    # points[nprow-1][a].lock()

# points[0][0].lock()
# points[int(nprow/4)-1][0].lock()
# points[int(3*nprow/4)-1][0].lock()
# points[int(2*nprow/4)-1][0].lock()
# points[nprow-1][0].lock()

# points[0][rows-1].lock()
# points[int(nprow/4)-1][rows-1].lock()
# points[int(3*nprow/4)-1][rows-1].lock()
# points[int(2*nprow/4)-1][rows-1].lock()
# points[nprow-1][rows-1].lock()

# points[0][int((rows-1)/4)].lock()
# points[0][int(2*(rows-1)/4)].lock()
# points[0][int(3*(rows-1)/4)].lock()
# points[0][int((rows-1))].lock()

# points[nprow-1][int((rows-1)/4)].lock()
# points[nprow-1][int(3*(rows-1)/4)].lock()
# points[nprow-1][int(2*(rows-1)/4)].lock()
# points[nprow-1][int((rows-1))].lock()

springs = []

for k in range(nprow):
    for l in range(rows):
        if k+1<=nprow-1:
            springs.append(Spring(points[k][l], points[k+1][l], 9, 800))
        if l+1<=rows-1:
            springs.append(Spring(points[k][l], points[k][l+1], 9, 800))

time = pygame.time.Clock()
run = True
while run:
    time.tick(240)
    screen.fill((70, 74, 120))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for s in springs:
        s.update()
        s.show(screen)

    for pi in points:
        for pj in pi:
            pj.show(screen)
            pj.applyforce(Vector2D(0, 700))
            pj.update()
            pj.edge([screen.get_width(), screen.get_height()])
            # print(screen.get_width(), screen.get_height())
    pygame.display.update()