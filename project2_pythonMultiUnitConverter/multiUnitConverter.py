conversion_history = []  # Global list to store conversion history

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def displayMenu():
    print("""\nWelcome to Multi-Unit Converter!
Choose a category to convert:

1) Weight
2) Temperature
3) Time
4) Length
5) Volume
h) Show Conversion History
q) Quit
""")

def getChoice():
    choice = input("Enter your choice: ").strip().lower()
    return choice

def handleChoice(choice):
    if choice == '1':
        weightConverter()
    elif choice == '2':
        temperatureConverter()
    elif choice == '3':
        timeConverter()
    elif choice == '4':
        lengthConverter()
    elif choice == '5':
        volumeConverter()
    elif choice == 'h':
        showHistory()
    elif choice == 'q':
        print("Goodbye")
        exit()
    else:
        print("\nInvalid Choice")

def weightConverter():
    while True:
        print("\nWeight Converter selected.")
        print("""Weight Conversions:
        1) Kilograms (kg) to Pounds (lb)
        2) Pounds (lb) to Kilograms (kg)
        3) Grams (g) to Ounces (oz)
        4) Ounces (oz) to Grams (g)
        b) Back to main menu
        """)
        
        sub_choice = input("Enter your choice: ").strip().lower()

        if sub_choice == '1': 
            kg = get_float_input("Enter weight in kilograms (kg) to be converted to pounds (lbs): ")
            pounds = kg * 2.20462
            result = f"Weight: {kg} kg is {pounds:.2f} lbs"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '2': 
            lb = get_float_input("Enter weight in pounds (lbs) to be converted to kilograms (kg): ")
            kg = lb / 2.20462
            result = f"Weight: {lb} lbs is {kg:.2f} kg"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '3':
            grams = get_float_input("Enter weight in grams (g) to be converted to ounces (oz): ")
            ounces = grams / 28.3495
            result = f"Weight: {grams} g is {ounces:.2f} oz"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '4':
            oz = get_float_input("Enter weight in ounces (oz) to be converted to grams (g): ")
            grams = oz * 28.3495
            result = f"Weight: {oz} oz is {grams:.2f} g"
            print(result)
            conversion_history.append(result)

        elif sub_choice == 'b':
            break
        else:
            print("Invalid choice. Please try again.")

def temperatureConverter():
    while True:
        print("\nTemperature Converter selected.")
        print("""Temperature Conversions:
        1) Celsius (°C) to Fahrenheit (°F)
        2) Fahrenheit (°F) to Celsius (°C)
        3) Celsius (°C) to Kelvin (K)
        4) Kelvin (K) to Celsius (°C)
        5) Fahrenheit (°F) to Kelvin (K)
        6) Kelvin (K) to Fahrenheit (°F)
        b) Back to main menu
        """)
        
        sub_choice = input("Enter your choice: ").strip().lower()

        if sub_choice == '1':
            c = get_float_input("Enter temperature in Celsius (°C): ")
            f = (c * 9/5) + 32
            result = f"Temperature: {c}°C is {f:.2f}°F"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '2':
            f = get_float_input("Enter temperature in Fahrenheit (°F): ")
            c = (f - 32) * 5/9
            result = f"Temperature: {f}°F is {c:.2f}°C"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '3':
            c = get_float_input("Enter temperature in Celsius (°C): ")
            k = c + 273.15
            result = f"Temperature: {c}°C is {k:.2f}K"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '4':
            k = get_float_input("Enter temperature in Kelvin (K): ")
            c = k - 273.15
            result = f"Temperature: {k}K is {c:.2f}°C"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '5':
            f = get_float_input("Enter temperature in Fahrenheit (°F): ")
            k = (f - 32) * 5/9 + 273.15
            result = f"Temperature: {f}°F is {k:.2f}K"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '6':
            k = get_float_input("Enter temperature in Kelvin (K): ")
            f = (k - 273.15) * 9/5 + 32
            result = f"Temperature: {k}K is {f:.2f}°F"
            print(result)
            conversion_history.append(result)

        elif sub_choice == 'b':
            break
        else:
            print("Invalid choice. Please try again.")

def timeConverter():
    while True:
        print("\nTime Converter selected.")
        print("""Time Conversions:
        1) Seconds to Minutes
        2) Minutes to Seconds
        3) Minutes to Hours
        4) Hours to Minutes
        5) Hours to Days
        6) Days to Hours
        7) Days to Weeks
        8) Weeks to Days
        b) Back to main menu
        """)

        sub_choice = input("Enter your choice: ").strip().lower()

        if sub_choice == '1':
            seconds = get_float_input("Enter time in seconds: ")
            minutes = seconds / 60
            result = f"Time: {seconds} seconds is {minutes:.2f} minutes"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '2':
            minutes = get_float_input("Enter time in minutes: ")
            seconds = minutes * 60
            result = f"Time: {minutes} minutes is {seconds:.2f} seconds"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '3':
            minutes = get_float_input("Enter time in minutes: ")
            hours = minutes / 60
            result = f"Time: {minutes} minutes is {hours:.2f} hours"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '4':
            hours = get_float_input("Enter time in hours: ")
            minutes = hours * 60
            result = f"Time: {hours} hours is {minutes:.2f} minutes"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '5':
            hours = get_float_input("Enter time in hours: ")
            days = hours / 24
            result = f"Time: {hours} hours is {days:.2f} days"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '6':
            days = get_float_input("Enter time in days: ")
            hours = days * 24
            result = f"Time: {days} days is {hours:.2f} hours"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '7':
            days = get_float_input("Enter time in days: ")
            weeks = days / 7
            result = f"Time: {days} days is {weeks:.2f} weeks"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '8':
            weeks = get_float_input("Enter time in weeks: ")
            days = weeks * 7
            result = f"Time: {weeks} weeks is {days:.2f} days"
            print(result)
            conversion_history.append(result)

        elif sub_choice == 'b':
            break
        else:
            print("Invalid choice. Please try again.")

def lengthConverter():
    while True:
        print("\nLength Converter selected.")
        print("""Length Conversions:
        1) Meters (m) to Feet (ft)
        2) Feet (ft) to Meters (m)
        3) Kilometers (km) to Miles (mi)
        4) Miles (mi) to Kilometers (km)
        5) Centimeters (cm) to Inches (in)
        6) Inches (in) to Centimeters (cm)
        b) Back to main menu
        """)

        sub_choice = input("Enter your choice: ").strip().lower()

        if sub_choice == '1':
            m = get_float_input("Enter length in meters: ")
            ft = m * 3.28084
            result = f"Length: {m} m is {ft:.2f} ft"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '2':
            ft = get_float_input("Enter length in feet: ")
            m = ft / 3.28084
            result = f"Length: {ft} ft is {m:.2f} m"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '3':
            km = get_float_input("Enter length in kilometers: ")
            mi = km * 0.621371
            result = f"Length: {km} km is {mi:.2f} mi"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '4':
            mi = get_float_input("Enter length in miles: ")
            km = mi / 0.621371
            result = f"Length: {mi} mi is {km:.2f} km"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '5':
            cm = get_float_input("Enter length in centimeters: ")
            inch = cm / 2.54
            result = f"Length: {cm} cm is {inch:.2f} in"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '6':
            inch = get_float_input("Enter length in inches: ")
            cm = inch * 2.54
            result = f"Length: {inch} in is {cm:.2f} cm"
            print(result)
            conversion_history.append(result)

        elif sub_choice == 'b':
            break
        else:
            print("Invalid choice. Please try again.")

def volumeConverter():
    while True:
        print("\nVolume Converter selected.")
        print("""Volume Conversions:
        1) Liters (L) to Gallons (gal)
        2) Gallons (gal) to Liters (L)
        3) Milliliters (mL) to Fluid Ounces (fl oz)
        4) Fluid Ounces (fl oz) to Milliliters (mL)
        b) Back to main menu
        """)

        sub_choice = input("Enter your choice: ").strip().lower()

        if sub_choice == '1':
            liters = get_float_input("Enter volume in liters: ")
            gallons = liters * 0.264172
            result = f"Volume: {liters} L is {gallons:.2f} gal"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '2':
            gallons = get_float_input("Enter volume in gallons: ")
            liters = gallons / 0.264172
            result = f"Volume: {gallons} gal is {liters:.2f} L"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '3':
            ml = get_float_input("Enter volume in milliliters: ")
            fl_oz = ml / 29.5735
            result = f"Volume: {ml} mL is {fl_oz:.2f} fl oz"
            print(result)
            conversion_history.append(result)

        elif sub_choice == '4':
            fl_oz = get_float_input("Enter volume in fluid ounces: ")
            ml = fl_oz * 29.5735
            result = f"Volume: {fl_oz} fl oz is {ml:.2f} mL"
            print(result)
            conversion_history.append(result)

        elif sub_choice == 'b':
            break
        else:
            print("Invalid choice. Please try again.")

def showHistory():
    print("\nConversion History:")
    if not conversion_history:
        print("No conversions done yet.")
    else:
        for i, entry in enumerate(conversion_history, 1):
            print(f"{i}) {entry}")
    input("\nPress Enter to return to main menu.")

# Main loop
while True:
    displayMenu()
    choice = getChoice()
    handleChoice(choice)
