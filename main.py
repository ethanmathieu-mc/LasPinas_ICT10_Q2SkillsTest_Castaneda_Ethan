# Skills test - 2nd Quarter
from pyscript import document

non_metals = {
    "Hydrogen": ("H", "Hydrogen", 1, 1.008),
    "Helium": ("He", "Helium", 2, 4.0026),
    "Carbon": ("C", "Carbon", 6, 12.011),
    "Nitrogen": ("N", "Nitrogen", 7, 14.007),
    "Oxygen": ("O", "Oxygen", 8, 15.999),
    "Fluorine": ("F", "Fluorine", 9, 18.998),
    "Neon": ("Ne", "Neon", 10, 20.180),
    "Chlorine": ("Cl", "Chlorine", 17, 35.453),
    "Argon": ("Ar", "Argon", 18, 39.948),
    "Krypton": ("Kr", "Krypton", 36, 83.798),
    "Xenon": ("Xe", "Xenon", 54, 131.293),
    "Radon": ("Rn", "Radon", 86, 222.018),
    "Bromine": ("Br", "Bromine", 35, 79.904),
    "Phosphorus": ("P", "Phosphorus", 15, 30.974),
    "Sulfur": ("S", "Sulfur", 16, 32.065),
    "Selenium": ("Se", "Selenium", 34, 78.960),
    "Iodine": ("I", "Iodine", 53, 126.904),
}

def element_checker(e):
    element1 = document.getElementById("element-symbol").value.strip().title()

    # Using .get() - no if statement
    result = non_metals.get(
        element1,
        ("N/A", "Element not found", "-", "-")
    )

    document.getElementById("result").innerHTML = f"""
        <b>Symbol:</b> {result[0]} <br>
        <b>Element:</b> {result[1]} <br>
        <b>Atomic Number:</b> {result[2]} <br>
        <b>Atomic Mass:</b> {result[3]} <br>
    """