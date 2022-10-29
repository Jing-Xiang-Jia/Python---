from pickletools import int4


age = int(input())
pay = int(input())


if age >=17 and age <24:
    total = pay - 300
elif age >=60 and age <80:
    total = pay - 500
else:
    total = pay

print(f'{total:,.0F}元')