token = str(input())
price = int(input())
amount = int(input())
total = price * amount

if token == "A":
    if total >=3000:
        total = total *0.8
    elif total >=2000:
        total = total *0.9
    else:
        total = total *0.95

elif token == "B":
    if total >=4000:
        total = total *0.75
    elif total >=3000:
        total = total *0.85

elif token == "C":
    total = total *0.9

print(f"{total:,.0f}元")
