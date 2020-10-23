# Gets an input for an temperature and unit to be converted and returns the temperature in other unit provided by the user
def getTemp(prompt):
    while True:
        try:
            userInput = int(input(prompt))
            break
        except ValueError:
            try:
                userInput = float(input(prompt))
                break
            except ValueError:
                print("Invalid input.\nEnter a valid numeric temperature: ")
                continue

    return userInput


def getUnit(prompt):
    while True:
        try:
            userInput = int(input(prompt))
        except ValueError:
            print("Invalid input\n")
            continue

        if userInput == 1:
            unit = "Celsius"
            break
        elif userInput == 2:
            unit = "Kelvin"
            break
        elif userInput == 3:
            unit = "Fahrenheit"
            break
        else:
            print("Enter a valid input\n")
            continue

    return unit


def tempConvert(inputTemp, inputUnit, returnUnit):

    if inputUnit == "Celsius":
        if returnUnit == "Kelvin":
            converted = inputTemp + 273.15
            return converted
        elif returnUnit == "Fahrenheit":
            converted = inputTemp * 1.8 + 32
            return converted

    elif inputUnit == "Kelvin":
        if returnUnit == "Celsius":
            converted = inputTemp - 273.15
            return converted
        elif returnUnit == "Fahrenheit":
            converted = inputTemp * 1.8 - 459.67
            return converted

    elif inputUnit == "Fahrenheit":
        if returnUnit == "Celsius":
            converted = (inputTemp - 32) / 1.8
            return converted
        elif returnUnit == "Kelvin":
            converted = (inputTemp + 459.67) / 1.8
            return converted


userTemp = getTemp("Insert a temperature to be converted: ")

userUnit = getUnit(
    "Select the original temperature Unit:\n1: Celsius\n2: Kelvin\n3: Fahrenheit\n> "
)

targetUnit = getUnit(
    "Select temperature unit to which you want to convert:\n1: Celsius\n2: Kelvin\n3: Fahrenheit\n> "
)

result = tempConvert(userTemp, userUnit, targetUnit)

print("\n{} {} is equivalent to {} {}".format(userTemp, userUnit, result, targetUnit))
