n = int(input())
current_number = 1

while current_number <= n:
    if (5 <= current_number <= 9) or (17 <= current_number <= 37) or (78 <= current_number <= 87):
        current_number += 1
        continue

    print(f"{current_number}")
    current_number += 1
