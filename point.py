class Point:
    counter = 0

    def __init__(self, name: int, x: float, y: float, z: float):
        Point.counter += 1
        self.id = Point.counter
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


    @staticmethod
    def create_point_from_list(data: list):
        if len(data) == 4:
            return Point(data[0], data[1], data[2], data[3])
        if len(data) == 3:
            return Point(Point.counter + 1, data[0], data[1], data[2])

    @staticmethod
    def create_point_from_input():
        data = input("Введите \"№ x y z\":").split()
        return Point.create_point_from_list(data)

    def __str__(self):
        return f"Точка № \"{self.name}\":\n" \
               f"\tx = {self.x}\n" \
               f"\ty = {self.y}\n" \
               f"\tz = {self.z}\n"
