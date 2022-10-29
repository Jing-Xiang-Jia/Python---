money = int(input())
hour = int(input())

if hour >= 50:
    total = money * hour +35*hour
elif hour <50 and hour >= 30:
    total = money * hour +25*hour
elif hour <30 and hour >= 10:
    total = money * hour +10*hour
else:
    total = money * hour

print(f'{total:,.0f}元')
