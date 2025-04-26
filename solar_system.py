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
        :return: None – Adds to planet list if valid, prints rejection if not.
        """

        self.planets.append(name) if name in self.valid_planets else print(f"{name}. You are not a real planet.")

    def remove_planet(self, name):
        """
        Attempts to remove a planet from the solar system.
        :param name: The name of the planet to remove.
        :return: None – Removes planet from list or prints error message.
        """

        self.planets.remove(name) if name in self.planets else print(f"{name} is not in the solar system.")