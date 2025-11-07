print(r"""
 _   _       _                          _   _   _       _ _     _____                           _            
| | | |     (_)                        | | | | | |     (_) |   /  __ \                         | |           
| | | |_ __  ___   _____ _ __ ___  __ _| | | | | |_ __  _| |_  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ 
| | | | '_ \| \ \ / / _ \ '__/ __|/ _` | | | | | | '_ \| | __| | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |_| | | | | |\ V /  __/ |  \__ \ (_| | | | |_| | | | | | |_  | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   
 \___/|_| |_|_| \_/ \___|_|  |___/\__,_|_|  \___/|_| |_|_|\__|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                                                                                             
""")


running = True

while running:
    print("\nSelect the unit you want to convert from:")
    print("1. Meter (m)")
    print("2. Kilometer (km)")
    print("3. Centimeter (cm)")
    print("4. Millimeter (mm)")
    print("5. Mile (mi)")
    print("6. Kilogram (kg)")
    print("7. Gram (g)")
    print("8. Milligram (mg)")
    print("9. Pound (lb)")
    print("10. Ounce (oz)")
    print("11. Celsius (°C)")
    print("12. Fahrenheit (°F)")
    print("13. Kelvin (K)")
    print("14. Liter (L)")
    print("15. Milliliter (mL)")
    print("16. Exit")

    from_unit = input("\nEnter your choice (1-16): ")

    # Check valid input
    if not from_unit.isdigit() or int(from_unit) < 1 or int(from_unit) > 16:
        print("Please select a number from 1-16.")
        input("Press Enter to return to the menu...")
        continue

    if from_unit == "16":
        print("Goodbye")
        break

    unit_names = {
    "1": "meters",
    "2": "kilometers",
    "3": "centimeters",
    "4": "millimeters",
    "5": "miles",
    "6": "kilograms",
    "7": "grams",
    "8": "milligrams",
    "9": "pounds",
    "10": "ounces",
    "11": "Celsius",
    "12": "Fahrenheit",
    "13": "Kelvin",
    "14": "liters",
    "15": "milliliters"
    }

    value_input = input(f"Enter the value ({unit_names[from_unit]}): ")

    # Check if empty OR not a valid number
    #.strip() removes any spaces at the beginning and end of a string.
    if not value_input.strip():
        print(f"Please enter a valid number for {unit_names[from_unit]}.")
        input("Press Enter to return to the menu...")
        continue

    value = float(value_input)


    # Show valid conversion options based on the chosen unit
    if from_unit in ["1", "2", "3", "4", "5"]:
        print("\nConvert TO:")
        print("1. Meter (m)")
        print("2. Kilometer (km)")
        print("3. Centimeter (cm)")
        print("4. Millimeter (mm)")
        print("5. Mile (mi)")
    elif from_unit in ["6", "7", "8", "9", "10"]:
        print("\nConvert TO:")
        print("6. Kilogram (kg)")
        print("7. Gram (g)")
        print("8. Milligram (mg)")
        print("9. Pound (lb)")
        print("10. Ounce (oz)")
    elif from_unit in ["11", "12", "13"]:
        print("\nConvert TO:")
        print("11. Celsius (°C)")
        print("12. Fahrenheit (°F)")
        print("13. Kelvin (K)")
    elif from_unit in ["14", "15"]:
        print("\nConvert TO:")
        print("14. Liter (L)")
        print("15. Milliliter (mL)")

    to_unit = input("Enter your target unit number: ")

        # Validate target unit selection based on category
    if from_unit in ["1", "2", "3", "4", "5"]:  # Length units
        valid_targets = ["1", "2", "3", "4", "5"]
    elif from_unit in ["6", "7", "8", "9", "10"]:  # Weight units
        valid_targets = ["6", "7", "8", "9", "10"]
    elif from_unit in ["11", "12", "13"]:  # Temperature units
        valid_targets = ["11", "12", "13"]
    elif from_unit in ["14", "15"]:  # Volume units
        valid_targets = ["14", "15"]

    if to_unit not in valid_targets:
        print("Please select only from the available choices above.")
        input("Press Enter to return to the menu...")
        continue


    # Check valid target input
    if not to_unit.isdigit():
        print("Please enter a number for the target unit.")
        input("Press Enter to return to the menu...")
        continue

    result = 0
    unit_name = ""

    # Length conversions
    if from_unit in ["1", "2", "3", "4", "5"]:
        if from_unit == "1":
            base = value
        elif from_unit == "2":
            base = value * 1000
        elif from_unit == "3":
            base = value / 100
        elif from_unit == "4":
            base = value / 1000
        elif from_unit == "5":
            base = value * 1609.34

        if to_unit == "1":
            result = base
            unit_name = "meters"
        elif to_unit == "2":
            result = base / 1000
            unit_name = "kilometers"
        elif to_unit == "3":
            result = base * 100
            unit_name = "centimeters"
        elif to_unit == "4":
            result = base * 1000
            unit_name = "millimeters"
        elif to_unit == "5":
            result = base / 1609.34

    # Weight conversions
    elif from_unit in ["6", "7", "8", "9", "10"]:
        if from_unit == "6":
            base = value
        elif from_unit == "7":
            base = value / 1000
        elif from_unit == "8":
            base = value / 1_000_000
        elif from_unit == "9":
            base = value * 0.453592
        elif from_unit == "10":
            base = value * 0.0283495

        if to_unit == "6":
            result = base
            unit_name = "kilograms"
        elif to_unit == "7":
            result = base * 1000
            unit_name = "grams"
        elif to_unit == "8":
            result = base * 1_000_000
            unit_name = "milligrams"
        elif to_unit == "9":
            result = base / 0.453592
            unit_name = "pounds"
        elif to_unit == "10":
            result = base / 0.0283495
            unit_name = "ounces"

    # Temperature conversions
    elif from_unit in ["11", "12", "13"]:
        if from_unit == "11":
            base = value
        elif from_unit == "12":
            base = (value - 32) * 5 / 9
        elif from_unit == "13":
            base = value - 273.15

        if to_unit == "11":
            result = base
            unit_name = "Celsius"
        elif to_unit == "12":
            result = (base * 9 / 5) + 32
            unit_name = "Fahrenheit"
        elif to_unit == "13":
            result = base + 273.15
            unit_name = "Kelvin"

    # Volume conversions
    elif from_unit in ["14", "15"]:
        if from_unit == "14":
            base = value
        elif from_unit == "15":
            base = value / 1000

        if to_unit == "14":
            result = base
            unit_name = "liters"
        elif to_unit == "15":
            result = base * 1000
            unit_name = "milliliters"

    print("\nResult:", result, unit_name)
    input("\nPress Enter to continue...")
