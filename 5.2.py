class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width
        
    
    def Perimeter(self):
        return 2*(self.length + self.width)
    
    def Area(self):
        return self.length*self.width   
    
    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())
class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        #super().__init__(length, width)
        self.height = height
        
    def volume(self):
        return self.length*self.width*self.height
        
myRectangle = Rectangle(7 , 5)
myRectangle.display()
myParallelepipede = Parallelepipede(7 , 5 , 2)
print("the volume of myParallelepipede is: " , myParallelepipede.volume())
