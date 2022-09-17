from math import *

class Vector():

    def __init__(self, *coords):
        if type(coords[0]) == int or type(coords[0]) == float:
            self.coords = coords
            self.len_coords = len(coords)
        elif type(coords[0]) == tuple:
            self.coords = coords[0]
            self.len_coords = len(coords[0])

    def lenght(self):
        '''Returns the length of the vector'''
        trunk = 0
        try:
            for coord in self.coords:
                trunk += (coord ** 2)
            return trunk ** (1 / 2)
        except:
            print("всё полетело")

    def scalar(self, other):
        ''' Returns the scalar product of vectors '''
        trunk = 0
        try:
            for i in range(len(self.coords)):
                trunk += self.coords[i] * other.coords[i]
            return trunk
        except:
            print("всё полетело")
        # return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def __add__(self, other):
        ''' Return self+other in the vector sense '''
        try:
            return Vector(tuple(self.coords[i] + other.coords[i] for i in range(self.len_coords)))
        except:
            print("всё полетело")
        # return Vector((self.x + other.x), (self.y + other.y), (self.z + other.z))

    def __sub__(self, other):
        ''' Return self+other in the vector sense '''
        try:
            for i in range(len(self.coords)):
                return Vector(tuple(self.coords[i] - other.coords[i] for i in range(self.len_coords)))
            return tuple(self.coords)
        except:
            print("всё полетело")
        # return self + (other * (-1))
        # return Vector((self.x - other.x), (self.y - other.y), (self.z - other.z))

    def __mul__(self, other):
        ''' Return self*other in the vector sense or self*scalar'''
        if type(other) == Vector:
            return Vector(tuple(self.coords[i] * other.coords[i] for i in range(self.len_coords)))
        elif type(other) == int or type(other) == float:
            return Vector(tuple(self.coords[i] + other for i in range(self.len_coords)))

    def __truediv__(self, other):
        ''' Return self/other in the vector sense or self/scalar'''
        if type(other) == Vector:
            return Vector(tuple(self.coords[i] / other.coords[i] for i in range(self.len_coords)))
        elif type(other) == int or type(other) == float:
            return Vector(tuple(self.coords[i] / other for i in range(self.len_coords)))

    def cos(self, other):
        ''' Return the cos value between two vectors '''
        trunk = 0
        try:
            return Vector(self.scalar(other) / (self.lenght() * other.lenght()))
        except:
            pass

    def is_collinear(self, other):
        ''' Checks vectors for collinearity '''
        try:
            print(abs(self.scalar(other)), (self.lenght() * other.lenght()))
            return (abs(self.scalar(other)) == (self.lenght() * other.lenght()))
        except:
            print("всё полетело")

    def co_directional(self, other):
        pass

    def __str__(self):
        trunk = ""
        for i in range(self.len_coords):
            trunk += str(self.coords[i]) + ", "
        return trunk[:-2]
