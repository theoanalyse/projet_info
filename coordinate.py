class Coordinate:
    def __init__(self, lat, lon, name):
        self.latitude = lat
        self.longitude = lon
        self.name = name

def get_coordinates(self):
    return tuple(self.latitude, self.longitude, self.name)