class SolarSystem:
    """
    Represents a Solar System containing a collection of valid planets.
    Allows adding and removing planets while validating against accepted planets.
    """
    def __init__(self):
        """
        Initializes the Solar System with:
        - An empty list of planets
        - A predefined list of valid planet names
        """
        self.planets = []
        self.valid_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    def add_planet(self, name):
        """
        Attempts to add a planet to the solar system.
        :param name: The name of the planet to add.
        :return: None – prints success or rejection message.
        """
        pass

    def remove_planet(self, name):
        """
        Attempts to remove a planet from the solar system.
        :param name: The name of the planet to remove.
        :return: None – prints success or error message.
        """
        pass