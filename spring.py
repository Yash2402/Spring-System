from vector2d import Vector2D
import pygame
dt = 0.001
class Point():
    def __init__(self, x, y, id):
        self.pos = Vector2D(x, y)
        self.vel = Vector2D(0.000001, 0.000001)
        self.acc = Vector2D(0.000001, 0.000001)
        self.mass = 10
        self.damp = Vector2D(0.000001, 0.000001)
        self.locked = False
        self.id = id
    def lock(self):
        self.locked = True
    def show(self, screen):
        if self.locked:
            pygame.draw.circle(screen, (255,0,0), self.pos.coordinates, 1)
        if not self.locked:
            pygame.draw.circle(screen, (255,255,255), self.pos.coordinates, 1)
    def applyforce(self, f):
        if not self.locked:
            self.acc = f.mult(1/self.mass)
    def update(self):
        self.damp = (self.vel.unit()).mult(-0.2)
        self.vel = self.vel.add(self.acc.mult(dt))
        self.vel = self.vel.add(self.damp.mult(dt))
        self.pos = self.pos.add(self.vel)
        self.acc = Vector2D(0, 0)
    def edge(self, dim):
        if self.pos.x > dim[0]:
            self.vel = Vector2D(-self.vel.coordinates[0], self.vel.coordinates[1])
        if self.pos.x < 0:
            self.vel = Vector2D(-self.vel.coordinates[0], self.vel.coordinates[1])
        if self.pos.y < 0:
            self.vel = Vector2D(self.vel.coordinates[0], -self.vel.coordinates[1])
        if self.pos.y > dim[1]:
            self.vel = Vector2D(self.vel.coordinates[0], -self.vel.coordinates[1])
class Spring():
    def __init__(self, a:Point, b:Point, restlength, k):
        self.a = a
        self.b = b
        self.restlength = restlength
        self.k = k
    def show(self, screen):
        pygame.draw.aaline(screen, (0, 0, 0), self.a.pos.coordinates, self.b.pos.coordinates)
    def update(self):
        x = -self.restlength + (self.a.pos.sub(self.b.pos)).mag()
        f = ((self.a.pos.sub(self.b.pos)).unit()).mult(self.k*x)
        self.a.applyforce(f.mult(-1))
        self.b.applyforce(f)
        self.a.update()
        self.b.update()