found_alexandra = False
people_between = 0

while True:
    name = input()
    
    if name == "Левон":
        break
        
    if found_alexandra:
        people_between += 1
        
    if name == "Александра":
        found_alexandra = True

print(f'{people_between} человек между Александрой и Левоном')
