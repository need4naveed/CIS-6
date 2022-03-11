import math

class Shape():
    def __init__(self):
        self.shape = 'shape'
    def __str__(self):
        return "I am a {}.".format(self.shape)

class Polygon(Shape):  
    def __init__(self):
        self.shape = 'polygon'
        self.side_lengths = None        
    def compute_perimeter(self):
        return sum(self.side_lengths)
    def get_number_of_edges(self):
        return len(self.side_lengths)

class Rectangle(Polygon):
    def __init__(self):
        self.shape = 'rectangle'
        self.side_lengths = [1, 1, 1, 1]

class Triangle(Polygon):
    def __init__(self):
        self.shape = 'triangle'
        self.side_lengths = [2, 2, 2] 
