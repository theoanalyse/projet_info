import math as m

EARTH_RADIUS = 6378137 # equatorial radius of earth in meters

class Coordinate:
    def __init__(self, x, y, name):
        self.x = x # latitude in degrees, will be deleted later
        self.y = y # longitude in degrees, will be deleted later
        self.phi = ( m.pi * x ) / 180 # latitude in radians
        self.theta = ( m.pi* y ) / 180 # longitude in radians
        self.name = name # name of the port     

    def get_name(self):
        return self.name

    def get_coordinates_degree(self):
        return (self.x, self.y, self.name)

    def get_coordinates_radians(self):
        return (self.phi, self.theta, self.name)

    def haversine(self, angle) :
        return m.sin(angle / 2)**2
        
    def distance(self, other): #returns distance between two cities in meters !
        phi1, theta1, name1 = self.get_coordinates_radians()
        phi2, theta2, name2 = other.get_coordinates_radians()
        return 2*EARTH_RADIUS*m.asin(m.sqrt(self.haversine(phi2-phi1) + m.cos(phi2) * m.cos(phi1) * self.haversine(theta2-theta1)))

'''
marseille = Coordinate(43.295224, 5.374439, "marseille")
paris = Coordinate(48.856551, 2.35107, "paris")
'''