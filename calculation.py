from point import *
from plane import *

p1 = [1, -2, 0]
p2 = [2, 0, -1]
p3 = [0,-1,2]
p4 = [1,2,3]

p1 = Point.create_point_from_list(p1)
p2 = Point.create_point_from_list(p2)
p3 = Point.create_point_from_list(p3)
p4 = Point.create_point_from_list(p4)

plane1 = Plane.create_plane_from_3_point(p1, p2, p3)
plane2 = Plane.fit_plane_to_point_arr([p1, p2, p3])

print(plane1)
print(plane2)

print(plane1.distance_calc(p4))
print(plane2.distance_calc(p4))