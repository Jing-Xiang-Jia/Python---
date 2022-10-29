seat = str(input())
amount = int(input())

if seat != "A":
    total = 300 *amount
else:
    total = 500*amount

print(f'{total:,.0F}元')
