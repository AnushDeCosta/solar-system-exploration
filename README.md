# Solar System Exploration – OOP Project

![Solar System](https://upload.wikimedia.org/wikipedia/commons/c/c3/Solar_sys8.jpg)

## Summary
Solar System Exploration is a Python-based project showcasing foundational Object-Oriented Programming (OOP) principles. It focuses on creating modular, reusable classes (`Planet` and `SolarSystem`) that model real-world solar system concepts such as adding and validating planets. This project demonstrates clean class design, validation logic, dynamic list management, and good Python best practices.

## Introduction
The Solar System project was designed as a way to apply core Python OOP skills in a fun, structured way. It includes:
- Defining meaningful classes with attributes and methods
- Validating input before adding to the system
- Managing dynamic collections of objects (planets)
- Implementing clean, Pythonic code with meaningful docstrings and comments

All logic is encapsulated in classes that can easily be extended, reused, and maintained.

> **Note**: This project was created as part of the Object-Oriented Programming Workshops for the Bachelor of Data Analytics (XBDA) degree at the University of South Australia (UniSA).

## Project Features
The program allows users to:
- **Create Planet objects** with specific names
- **Create a Solar System** that can hold multiple Planet objects
- **Validate planets** to ensure only real (pre-approved) planets can be added
- **Dynamically add or remove planets** from the Solar System
- **Display the list of planets** in the Solar System

### Core Mechanics
- A predefined list of valid planets (e.g., Mercury, Venus, Earth) is checked before adding.
- Planets are stored inside the SolarSystem class using a list.
- Print statements inform users of success or validation failure when attempting to add planets.

### Validation Logic
- Only planets from a pre-approved list can be added.
- Invalid planets are rejected with a helpful message.

## Tools
- Python 3.13
- PyCharm, VSCode, or any Python IDE
- GitHub for version control

## Files
- `planet.py` – Defines the `Planet` class (with basic attributes like `name`).
- `solar_system.py` – Defines the `SolarSystem` class (manages a collection of planets).
- `README.md` – Project documentation.

## Usage
To use the classes:
- Import the `Planet` and `SolarSystem` classes into a Python file or an interactive terminal.
- Create a SolarSystem object and add Planet objects by calling its methods.

Example basic usage:

```python
from planet import Planet
from solar_system import SolarSystem

# Create a new Solar System
my_solar_system = SolarSystem()

# Create some Planet objects
earth = Planet("Earth")
mars = Planet("Mars")
jupiter = Planet("Jupiter")
pluto = Planet("Pluto")  # Note: Pluto is not a valid planet!

# Add planets to the Solar System
my_solar_system.add_planet(earth)
my_solar_system.add_planet(mars)
my_solar_system.add_planet(jupiter)
my_solar_system.add_planet(pluto)  # This should trigger a validation warning

# Remove a planet
my_solar_system.remove_planet(mars)

# Display the current Solar System
print(my_solar_system)
```
## Future Enhancements
- Add features like moons orbiting planets
- Simulate planet orbits and distances
- Expand the list to include dwarf planets (e.g., Pluto)
- Build a text-based exploration game

## License
This project is intended for educational purposes only as part of coursework for the University of South Australia (UniSA) Bachelor of Data Analytics (XBDA) degree.  
© 2025 Anush De Costa.

## Acknowledgements
This project was developed as part of the Week 3 Object-Oriented Programming (OOP) Workshops for the Bachelor of Data Analytics (XBDA) degree at UniSA.

Special thanks to the UniSA teaching team for their guidance on best practices in class design, modularity, and Python programming.
