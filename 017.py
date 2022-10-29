amount = str(input())

if amount[0]in["A","F","K"]:
    if amount[-2:] in ["21","32","50"]:
        print(f"{5000:,.0f}元")
    elif amount[-2:] in ["43","66","89"]:
        print(f"{4000:,.0f}元")
    elif amount[-2:] in ["85","10","12"]:
        print(f"{3000:,.0f}元")
    else:
        print(f"{0:,.0f}元")
elif amount[0]in["M","P","Q"]:
    if amount[-2:] in ["45","61","23"]:
        print(f"{5000:,.0f}元")
    elif amount[-2:] in ["89","77","32"]:
        print(f"{4000:,.0f}元")
    elif amount[-2:] in ["24","54","36"]:
        print(f"{3000:,.0f}元")
    else:
        print(f"{0:,.0f}元")
elif amount[0]in["R","U","V"]:
    if amount[-2:] in ["76","90","21"]:
        print(f"{5000:,.0f}元")
    elif amount[-2:] in ["56","81","50"]:
        print(f"{4000:,.0f}元")
    elif amount[-2:] in ["20","31","41"]:
        print(f"{3000:,.0f}元")
    else:
        print(f"{0:,.0f}元")
else: 
    print(f"{0:,.0f}元")