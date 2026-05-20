from math import cos, sin, pi
import openpyscad as ops


class Shapes2D:

    @staticmethod
    def regular_polygon(n, r):
        points = []
        for i in range(n):
            angle = i * 2 * pi / n
            points.append([r * cos(angle), r * sin(angle)])
        return ops.Polygon(points)

    @staticmethod
    def star(n, radii):
        points = []
        for i in range(n):
            angle = i * 2 * pi / n
            r = radii[i % len(radii)]
            points.append([r * cos(angle), r * sin(angle)])
        return ops.Polygon(points)