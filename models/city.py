class City:
    def __init__(self, name, lat=None, lon=None):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"City({self.name}, lat={self.lat}, lon={self.lon})"
