from point import *

class Plane:
    counter = 1

    def __init__(self, a: float, b: float, c: float, d: float):
        self.id = Plane.counter
        self.name = None
        self.number_of_points = 0
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        Point.counter += 1

    def __str__(self):
        return f"Поверхность \"{self.name}\":\n" \
               f"\tA = {self.a}\n" \
               f"\tB = {self.b}\n" \
               f"\tC = {self.c}\n" \
               f"\tD = {self.d}\n"

    def distance_calc(self, point: Point):
        return (abs((self.a * point.x) + (self.b * point.y) + (self.c * point.z) +
                    self.d) / (((self.a ** 2) + (self.b ** 2) + (self.c ** 2)) ** (0.5)))

    @staticmethod
    def create_plane_from_3_point(p1: Point, p2: Point, p3: Point):
        temp_plane = Plane(0, 0, 0, 0)
        temp_plane.name = f"Плоскость проходящая через точки: \"{p1.name}-{p2.name}-{p3.name}\""
        temp_plane.number_of_points = 3

        temp_plane.a = -((p2.y - p1.y) * (p3.z - p1.z) - (p3.y - p1.y) * (p2.z - p1.z))
        temp_plane.b = ((p2.x - p1.x) * (p3.z - p1.z) - (p3.x - p1.x) * (p2.z - p1.z))
        temp_plane.c = -((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y))
        temp_plane.d = -(p1.x*temp_plane.a + p1.y*temp_plane.b + p1.z*temp_plane.c)
        return temp_plane

    @staticmethod
    def fit_plane_to_point_arr(pointArr: list):
        import numpy as np
        xyz = np.array([[i.x, i.y, i.z] for i in pointArr])

        a1, b1, c1, d1, b2, c2, c3, d1, d2, d3 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for line in xyz:
            a1 += line[0] ** 2
            b1 += line[0] * line[1]
            c1 += line[0]
            b2 += line[1] ** 2
            c2 += line[1]
            c3 += 1
            d1 += line[0] * line[2]
            d2 += line[1] * line[2]
            d3 += line[2]

        mA = np.array([[a1, b1, c1], [b1, b2, c2], [c1, c2, c3]])
        mD = np.array([d1, d2, d3])
        abc = np.linalg.solve(mA, mD)

        temp_plane = Plane(0, 0, 0, 0)
        temp_plane.name = f"Поверхность {temp_plane.id} вписанная в массив точек"
        temp_plane.number_of_points = len(pointArr)
        temp_plane.a = abc[0]
        temp_plane.b = abc[1]
        temp_plane.c = -1
        temp_plane.d = abc[2]
        return temp_plane
