class Rectangle:
    def __init__(self, length, width):
        if((type(length) is int) and (type(width) is int)):
           self.length = length
           self.width = width
        else:
            raise Exception("data type not supported")

    def __iter__(self):
        yield from [
            {"length":self.length},
            {"width":self.width}
            ]



def iterateOver(rectInstance):
    for attrs in rectInstance:
        print(attrs)



        
# creating rectangle class objects
try:
    rect1 = Rectangle(12, 13)
    rect2 = Rectangle(23, 44)
    rect3 = Rectangle('lakshya', 23)
except Exception as e:
    print(e)

    
# iterating over the class instances
iterateOver(rect1)
iterateOver(rect2)
