class Qimat:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 2 * 3.14 * self.radius ** 2
    def get_diameter(self):
        return 2 * self.radius
    def get_circumference(self):
        return 2 * 3.14 * self.radius
    def get_radius(self):
        return self.radius

radius_value = float(input())
num = Qimat(radius_value)
print(num.get_area())
print(num.get_diameter())
print(num.get_circumference())
print(num.get_radius())