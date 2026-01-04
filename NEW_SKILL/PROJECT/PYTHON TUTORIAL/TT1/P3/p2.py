num=int(input("enter a num:"))
if num<0:
    its="negative"
elif num>0:
    its="postive"
else:
    its="zero"

print(its)

for i in range (1,num):
    print(i)