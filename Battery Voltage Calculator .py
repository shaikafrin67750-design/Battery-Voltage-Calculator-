# Battery Voltage Calculator

print("===== BATTERY VOLTAGE CALCULATOR =====")

voltage = float(input("Enter voltage of one battery (V): "))
number = int(input("Enter number of batteries: "))

total_voltage = voltage * number

print("\n===== RESULT =====")
print("Voltage of One Battery =", voltage, "V")
print("Number of Batteries =", number)
print("Total Battery Voltage =", round(total_voltage, 2), "V")