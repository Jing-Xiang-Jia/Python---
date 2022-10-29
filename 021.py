height = float (input())
weight=float(input())
second = float(input())

bmi = weight / (height**2)
if bmi >=19 and bmi<=21 or second <=13.5:
    print("符合條件")
else:
    print("不符合條件")