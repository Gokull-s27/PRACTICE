def stud():
    name=input("enter ur name")
    roll_num=int(input("enter ur ROLL_NUM"))
    num_of_sub=5
    Marks=[]
    for i in range(0,num_of_sub):

        while True:
            try:
                M=int(input(f"Enter ur mark{i+1}: "))
                if 0<=M<=100:
                    break
                else:
                    print("num exceeds total...pls enter again")
            except ValueError:
                print("invalid...try again")
                    
                
        Marks.append(M)

    total=sum(Marks)
    if total>=450:
        Grade="A"
    elif total >=400:
        Grade="B"
    elif total >=300:
        Grade="C"
    elif total >=200:
        Grade="D"
    else:
        Grade="C"

    print("---------RESULT----------")
    print(f"NAME      :     {name}")
    print(f"Roll      :     {roll_num}")
    print(f"MARKS     :     {Marks}")
    print(f"TOTAL     :     {total}")
    print(f"AVG       :     {total/num_of_sub}")
    print(f"GRADE     :     {Grade}")
    if Grade ==("A","B","C"):
        result="Pass"
    else:
        result="fail"
    print(f"RESULT    :     {result}")
    print("-------------------------")

    return {
        "name": name,
        "roll": roll_num,
        "marks": Marks,
        "total": total,
        "avg": total/num_of_sub,
        "grade": Grade,
        "result": result
    }

students=[]
while True:
    students.append(stud())
    again=input("Do you want to add another student? (y/n): ").lower()
    if again=="n":
        break
    elif again=="y":
        students.append(stud())
    else:
        print("invalid input")

print(students)

print("-----------ALL STUDENTS----------")
for i,s in enumerate(students,start=1):
    print(f"{i}{s['name']} (Roll: {s['roll']} -->)Grade :{s['grade']} | {s['result']}")






# name=input("enter ur name")
# roll_num=int(input("enter ur ROLL_NUM"))
# num_of_sub=5
# Marks=[]
# for i in range(0,num_of_sub):
#     M=int(input(f"Enter ur mark{i+1}: "))
#     Marks.append(M)

# print(Marks)
# total=sum(Marks)
# print(total)
# print(sum(Marks) /num_of_sub)

# if total>=90:
#     Grade="A"
# elif total >=75:
#     Grade="B"
# elif total >=60:
#     Grade="C"
# elif total >=40:
#     Grade="D"
# else:
#     Grade="C"

# print("grade:",Grade)

# print("---------RESULT----------")
# print(f"NAME      :     {name}")
# print(f"Roll      :     {roll_num}")
# print(f"MARKS     :     {Marks}")
# print(f"TOTAL     :     {total}")
# print(f"AVG       :     {total/num_of_sub}")
# print(f"GRADE     :     {Grade}")

# if Grade ==("A","B","C"):
#     result="Pass"
# else:
#     result="fail"

# print(f"RESULT    :     {result}")
# print("-------------------------")


