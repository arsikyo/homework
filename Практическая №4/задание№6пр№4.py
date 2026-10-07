import math

x_deg = float(input())
x_rad = math.radians(x_deg)
result = math.sin(x_rad) + math.cos(x_rad) + (math.tan(x_rad) ** 2)

print(result)