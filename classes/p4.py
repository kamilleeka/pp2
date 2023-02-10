from math import sqrt
a = int(input())
b = int(input())
class Point():
    def __init__(self, point1, point2):
        self.point1 = a
        self.point2 = b

    def Show(self):
        print(self.point1, self.point2)

    def Move(self):
        a1 = int(input())
        b1 = int(input())
        self.point1 = a1
        self.point2 = b1

    def Dist(self):
        dist = sqrt(pow(self.point1, 2) + pow(self.point2, 2))
        print(dist)


cl = Point(a, b)
cl.Dist()
cl.Show()
cl.Move()

