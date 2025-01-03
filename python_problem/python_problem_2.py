students = []

##############  menu 1 사전에 학생 정보 저장하는 코딩
def Menu1(name, score1, score2):
    students.append({"name": name, "score1": score1, "score2": score2, "grade": None})

##############  menu 2 학점 부여하는 코딩
def Menu2():
    for student in students:
        Score1 = int(student["score1"])
        Score2 = int(student["score2"])
        if student["grade"] is None:
            avg = ( Score1 + Score2) / 2
            if avg >= 90:
                student["grade"] = "A"
            elif avg >= 80:
                student["grade"] = "B"
            elif avg >= 70:
                student["grade"] = "C"
            else:
                student["grade"] = "D"

##############  menu 3 출력 코딩
def Menu3():
    print("---------------------------------")
    print("\nname\tmid\tfinal\tgrade")
    print("---------------------------------")
    for student in students:
        print(f"{student['name']}\t{student['score1']}\t{student['score2']}\t{student['grade']}")

##############  menu 4 학생 정보 삭제하는 코딩
def Menu4(name):
    global students
    students = [student for student in students if student["name"] != name]

# 메인
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True:
    try:
        choice = input("Choose menu 1, 2, 3, 4, 5 : ")

        if choice == "1":
            data = input("Enter name mid-score final-score : ").split()
            if len(data) != 3:
                raise ValueError("Num of data is not 3!")

            name, score1, score2 = data[0], data[1], data[2]
            if any(student["name"] == name for student in students):
                raise ValueError("Already exist name!")

            if not score1.isdigit() or not score2.isdigit():
                raise ValueError("Scores is not positive integer!")
            
            s1 = int(score1)
            s2 = int(score2)
            if s1 > 100 or s2 > 100:
                raise ValueError("Scores is not positive integer!")

            Menu1(name, score1, score2)


        elif choice == "2":
            if not students:
                raise ValueError("No student data!")
            else:
                Menu2()
                print("Grading to all students.")

        elif choice == "3":
            if not students:
                raise ValueError("No student data!")
            elif any(student["grade"] is None for student in students):
                raise ValueError("There is a student who didn't get grade.")
            else:
                Menu3()

        elif choice == "4":
            if not students:
                raise ValueError("No student data!")
            else:
                name = input("Enter the name to delete : ")
                if not any(student["name"] == name for student in students):
                    raise ValueError("Not exist name!")
                else:
                    Menu4(name)
                    print(f"{name} student information is deleted.")

        elif choice == "5":
            print("Exit Program!")
            break

        else:
            raise ValueError("Wrong number. Choose again.")
        
    except ValueError as e:
        print(e)