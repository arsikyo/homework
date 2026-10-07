price=int(input())
coin_count=0

while price>0:
    if price>=25:
        price-=25
    
    elif price>=10:
        price-=10
    
    elif price>=5:
        price-=5
    
    else:
        price-=1

    coin_count+=1

print(f'Ведьмаку надо заплатить {coin_count} монет')