# num=int(input("enter:"))
# while num<0 or num >=100:
#    print("nahh")
#    num=int(input("enter again :"))
# print("ur num",num)

while True:
    try:
        num=int(input("enter:"))
        if num<0 or num <=100:
            break
        else:
            print("invalid range")
    except ValueError:
        print("not a number")

print("ur num",num)