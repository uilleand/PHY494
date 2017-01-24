k_in = input ("Initial temperature in Kelvin? --> ")
k = float(k_in)

f_in = input ("Temperature change in Farenheit? --> ")
f = float(f_in)

f_delta = ((5./9)*f)

k_final = f_delta + k
print(k_final)
