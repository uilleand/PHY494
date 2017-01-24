# temperature conversion
temp_Kelvin = []
temperatures = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0]
for theta in temperatures:
   T = (theta - 32) * (5/9) + 273.15
   temp_Kelvin.append(T)

print("Conversion complete")
print(temp_Kelvin)
