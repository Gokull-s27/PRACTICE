def search_student(students,roll_no):
    for i in students:
        if i["roll"] == roll_no:
            return i
    return None

students = [{"name": "arun", "roll": 1, "total": 420},{"name": "raju", "roll": 2, "total": 450},{"name": "Goka", "roll": 3, "total": 390}]

roll_search = int(input("Enter roll_search: "))
result = search_student(students, roll_search)

if result is not None:
    print("Student Found")
    print("Name :", result["name"])
    print("Roll :", result["roll"])
    print("Total:", result["total"])
else:
    print("Student not found")