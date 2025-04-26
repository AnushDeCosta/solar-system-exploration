from planet import Planet

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

    def add_planet(self, planet):
        """
        Attempts to add a planet to the solar system.
        :param planet: The name of the planet to add.
        :return: None – Adds to planet list if valid, prints rejection if not.
        """

        self.planets.append(planet) if planet.name in self.valid_planets else print(f"----------\nL {planet.name}. You are not a real planet.\n")

    def remove_planet(self, planet):
        """
        Attempts to remove a planet from the solar system.
        :param planet: The name of the planet to remove.
        :return: None – Removes planet from list or prints error message.
        """

        self.planets.remove(planet) if planet in self.planets else None # print(f"{planet.name} is not in the solar system.")

    def __str__(self):
        """
        Returns a string representation of the solar system.
        Lists all added planets, or indicates if no planets exist.
        :return: Formatted string of planet names.
        """
        output = ["Planets in our Solar System:"]
        if not self.planets:
            output.append("(no planets yet)")
        else:
            for planet in self.planets:
                output.append(str(planet))
        return "\n".join(output)


