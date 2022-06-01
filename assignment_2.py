class Rectangle():

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def perimeter(self):
        return 2*(self.length+self.width)

    def area(self):
        return self.length*self.width

    def display(self):
        return "\n Length: {}\n Width: {}\n Perimeter: {}\n Area: {}".format(self.length,self.width,self.perimeter(),self.area())


class Parallelepipede(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height

    def volume(self):
        return self.height*self.width*self.length


        




emrah=Parallelepipede(2,3,4)
print(emrah.volume())
# print(emrah.perimeter())
# print(emrah.area())