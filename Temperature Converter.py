#Take a temperature value in Celsius from the user and convert it into Fahrenheit,kelvin. (Formula: \(F = (C \times 9/5) + 32\), \(K = C + 273.15\))
a=float(input("enter a temperature in celsius:"))
f=(a*9/5)+32
k=a+273.15
print(f"temperature in fahrenheit is {f}")
print(f"temperature in kelvin is {k}")
