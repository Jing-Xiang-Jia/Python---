amount = str(input())
list = ["1","3","7","8"]
list1 = ["3","5","9"]

if amount[0] in list and amount[1]in list1 or amount[-1] =="0":
    print("中獎")
else:
    print("沒中獎")