# Welcome user 
print()
print("====================")
print("Welcome to the UMBC")
print("Car Customization Form!")
print("====================")
print()

# Ask user what make and model they want
print("~ Make and Model ~")
print("1. What make and model of car would you like? ")
print(" a. Heavy Coquette")
print(" b. Bord Stallion")
print(" c. Bam 150")
print(" d. Tumble Joyce Ghost")
print()
makemodel = input("Please enter 'a' - 'd': ")

# Ask user what color car they want
print()
print("~ Exterior Color ~")
print("2. What color car do you want? ")
print()
exterior = input("Please enter your color choice: ")

# Ask user about moon roof
print()
print("~ Moonroof Option ~")
print("3. Would you like a moonrooof?")
print()
moonroof = input("Please enter 'yes' or 'no': ")

# Ask user which package they would like
print()
print("~ Package Upgrades ~ ")
print("4. Which package would you like to upgrade to? ")
print(" a. Off-road")
print(" b. GT performance")
print(" c. Winter")
print(" d. Premium")
print()
package = input("Please enter 'a' - 'b': ")

# Ask user about navigation with touch screen
print()
print("~ Navigation ~ ")
print("5. Would you like navigation with a touchscreen? ")
print()
touchscreen = input("Please enter 'yes' or 'no': ")

# Ask user what color interiror they want
print()
print("~ Interior Color ~ ")
print("6. What color interior do you want? ")
print()
interior = input("Please enter your color choice: ")

# Print the users summary
print()
print("~ Summary ~ ")
print()
print(f"Make and model option: {makemodel}")

print(f"Exterior color: {exterior}")

print(f"Moonroof Option: {moonroof}")

print(f"Package Upgrade: {package}")

print(f"Navigation: {touchscreen}")

print(f"Interior Color: {interior}")