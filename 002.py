amount = int(input())

if amount >= 200:
    total = int(0.65 * amount *0.9)

else:
    total = int(0.65 * amount)
    
print(f'{total:,.0f}元')