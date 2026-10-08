es = {i**5: i for i in range(1, 151)}
found = False

for a in range(1, 151):
    if found: break
    a5 = a**5
    
    for b in range(a, 151):
        if found: break
        b5 = b**5
        
        for c in range(b, 151):
            if found: break
            c5 = c**5
            
            for d in range(c, 151):
                current_sum = a5 + b5 + c5 + d**5
                
                if current_sum in es:
                    e = es[current_sum]
                    print(f"Ответ: a={a}, b={b}, c={c}, d={d}, e={e}")
                    print(f"Сумма: {a + b + c + d + e}")
                    found = True
                    break
