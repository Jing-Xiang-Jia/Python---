seat = str(input())
amount = int(input())

list = ["T","M","L","N"]

if seat[0] in list :
    total = 400 *amount
else:
    total = 500*amount

print(f'{total:,.0F}元')
