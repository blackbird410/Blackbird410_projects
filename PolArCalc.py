#!\bin\env python

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, input_width):
        self.width = input_width
        
    def set_height(self, input_height):
        self.height = input_height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height) 
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
            
        w = "*" * self.width
        return "\n".join([w] * self.height)
    
    def get_amount_inside(self, o_shape):
        return self.get_area // o_shape.get_area
        
    def __repr__(self):
        return f"{self.__name__}(width={self.width}, height={self.height}"
    

class Square(Rectangle):
    
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def set_side(self, s):
        self.set_width = s
        self.set_height = s
    
    def __repr__(self):
        return f"{self.__name__}(side={self.width})"
     