seat = str(input())
amount = int(input())

list = ["A","C","E","F","K"]

if seat in list :
    total = 350 *amount
else:
    total = 550*amount

print(f'{total:,.0F}元')
