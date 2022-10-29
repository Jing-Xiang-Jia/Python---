seat = str(input())
amount = int(input())

if seat == "A":
    total = 500 *amount
elif seat == "B":
    total = 450 *amount
elif seat == "C":
    total = 380 *amount
elif seat == "D":
    total = 310 *amount
elif seat == "E":
    total = 250 *amount

print(f'{total:,.0F}元')
