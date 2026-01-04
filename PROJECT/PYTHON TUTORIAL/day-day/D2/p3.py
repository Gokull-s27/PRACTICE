marks=[20,42,24,54,76]
#add==>marks.append(num)
#add==>marks.insert(index,num)

#remove==>marks.remove(num)
#remove==>marks.pop(index)
#remove==>clear()

#lenght==>len(marks)

name=input("enter ur name")
marks=[]

S_num=int(input("total num of subjects:"))
for i in range(0,S_num):
    m=float(input(f"enter marks of subject {i+1}:"))
    marks.append(m)
for k in marks:
    print(k)

while True:
    choice = input("\nDo you want to add/remove/update a mark? (1/2/3): ")

if choice == "1":
    addd=sum(marks)
    print(addd)
elif choice == "2":
    rem=float("enter num to remove:")
    marks.remove(rem)
elif choice == "3":
    add=("enter a num toaddd:")
    marks.append(add)
else:
    print("invalid choice")

for k in marks:
    print(k)


