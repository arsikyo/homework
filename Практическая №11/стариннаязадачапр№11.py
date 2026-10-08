for b in range(11):
    for k in range(21):
        for t in range(201):
            if b+k+t<1:
                continue
            elif 10*b+5*k+0.5*t==100:
                print(f'На 100 рублей можно купить {b} быка, {k} коров, {t} телят.')