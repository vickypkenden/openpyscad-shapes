import openpyscad as ops
from openpyscad_shapes_2d import Shapes2D
from openpyscad_shapes_3d import Shapes3D


if __name__ == "__main__":

    hexagon = Shapes2D.regular_polygon(6, 10)
    star = Shapes2D.star(10, [10, 5])
    dice = Shapes3D.dice(edge=15)

    model = ops.Union()
    model.append(hexagon)
    model.append(star)
    model.append(dice)

    model.write("output/model.scad")