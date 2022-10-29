amount = int(input())
total = amount * 55

if amount >= 4:
    total = 55 * amount + 0

else:
    total = 55 * amount + 60

print(f'{total:,.0f}元')