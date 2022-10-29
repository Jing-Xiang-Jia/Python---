amount = int(input())

if amount >=100000:
    total = int(amount *0.215)
elif amount<100000:
    total = int(amount*0.165)
print(f'{total:,.0f}元')