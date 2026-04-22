"""Temperature conversion utilities.

Provides functions to convert between Celsius and Fahrenheit.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    # Simple demonstration
    c = 100.0
    f = 212.0
    print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
