amount = str(input())
chinese = int(input())
EN = int(input())
math = int(input())



if amount == "1":
    total = chinese*1.5+EN*2+math*1.5
elif amount == "2":
    total = chinese*2+EN*1.5+math*1
elif amount == "3":
    total = chinese*1.5+EN*1.5+math*1
elif amount == "4":
    total = chinese*1+EN*1+math*2

print(total)
