import openpyscad as ops


class Shapes3D:

    @staticmethod
    def dice(edge=15, fn=32):
        edge = float(edge)

        cube = ops.Cube(edge, center=True)
        sphere = ops.Sphere(edge * 3 / 4, center=True)
        dice = cube & sphere

        c = ops.Circle(edge / 12, _fn=fn)
        h = 0.7
        point = c.linear_extrude(height=h)

        point1 = point.translate([0, 0, edge / 2 - h / 2])

        return dice - point1