import math
class Circle :
    def ___init__(self, name, radius, PI) :
        self.name = name
        self.radius = radius
        self.PI = PI
    
    
    def area(self):
        return self.PI * self.radius**2

        
    def __del__(self):
        pass


c1 = Circle('원' , 10 , math.pi)
c1.area()

c2 = Circle('원' , 200 , math.pi)
print('c2의 면적은 {}'.format(c2.area()))

print(math.tau)