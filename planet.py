import math

class Planet:
    """
    Represents a planet with its physical and orbital characteristics.
    """
    def __init__(self, name, mass, diameter, density, gravity, distance_from_sun, mean_temperature, moon_count, ring_system, global_magnetic_field):
        """
        Initialises a Planet with its physical and orbital attributes.
        :param name: Name of the planet (str)
        :param mass: Mass of the planet in 10^24 kg (float)
        :param diameter: Diameter of the planet in kilometres (int)
        :param density: Density of the planet in kg/m³ (float)
        :param gravity: Surface gravity in m/s² (float)
        :param distance_from_sun: Distance from the Sun in 10^6 km (float)
        :param mean_temperature: Average surface temperature in °C (int)
        :param moon_count: Number of moons (int)
        :param ring_system: Presence of ring system (bool)
        :param global_magnetic_field: Presence of a global magnetic field (bool)
        """
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.density = density
        self.gravity = gravity
        self.distance_from_sun = distance_from_sun
        self.mean_temperature = mean_temperature
        self.moon_count = moon_count
        self.ring_system = ring_system
        self.global_magnetic_field = global_magnetic_field

    def radius(self):
        """
        Calculates the radius of the planet based on its diameter.
        :return: The calculated radius of the planet.
        """
        radius = self.diameter/2
        return radius

    def surface_area(self):
        """
        Calculates the surface area of the planet based on its radius.
        :return: The surface area rounded to 2 decimal places.
        """
        surface_area = 4 * math.pi * (self.radius()) ** 2
        return round(surface_area, 2)

    def calculate_mass(self, weight):
        """
        A method to calculate your mass in newtons
        :param weight:
        :return:
        """
        pass

    def calculat_weight(self, weight):
        """
        A method to calculate your weight on certain planets
        :param weight:
        :return:
        """
        pass
