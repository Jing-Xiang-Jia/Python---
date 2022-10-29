height = float(input())
weight = float(input())

bmi = weight / (height**2)

if bmi >=18.5 and bmi <24:
    print("正常")
else:
    print("太輕或太重")