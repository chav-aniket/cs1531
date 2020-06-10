from math import sqrt, atan2, cos, sin, isclose, pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.theta = atan2(y, x)
        # self.r = sqrt(x**2 + y**2)

    @property
    def r(self):
        return sqrt(self.x**2+self.y**2)

    @property
    def theta(self):
        return atan2(self.y, self.x)

    # @property
    # def x(self):
    #     return self.r*cos(self.theta)

    # @property
    # def y(self):
    #     return self.r*sin(self.theta)

    @r.setter
    def r(self, r):
        self.x, self.y = r*cos(self.theta), r*sin(self.theta)

    @theta.setter
    def theta(self, theta):
        self.x, self.y = self.r*cos(theta), self.r*sin(theta)

    # @x.setter
    # def x(self, x):
    #     self.theta, self.r = atan2(self.y, x), sqrt(x**2 + self.y**2)

    # @y.setter
    # def y(self, y):
    #     self.theta, self.r = atan2(y, self.x), sqrt(self.x**2 + y**2)

def distance(start, end):
    '''
    Calculate the distance between 2 points.
    '''
    return sqrt((end.x - start.x)**2 + (end.y - start.y**2))

def test_point():
    me = Point(1, 1)
    my_house = Point(2, 1)
    assert isclose(distance(me, my_house), 1, rel_tol=0.01) # Within 1% tolerance
    me.x = 2
    assert isclose(distance(me, my_house), 0, rel_tol=0.01)
    me.y = 0
    assert isclose(me.r, 2, rel_tol=0.01)
    assert isclose(me.theta, 0, rel_tol=0.01)
    me.r = 3
    assert isclose(me.x, 3, rel_tol=0.01)
    me.theta = pi*0.25 # 45 degrees in radians
    assert isclose(me.x, 3*cos(pi*0.25), rel_tol=0.01)
    assert isclose(me.y, 3*cos(pi*0.25), rel_tol=0.01)
