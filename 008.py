chinese = int(input())
EN = int(input())
math = int(input())
social = int(input())
tech = int(input())

total = chinese+EN +math+social+tech
if total >=460 and total <=500:
    print("A")
elif total >=420 and total <=459:
    print("B")
elif total >=370 and total <=419:
    print("C")
elif total >=320 and total <=369:
    print("D")
elif total <320:
    print("E")