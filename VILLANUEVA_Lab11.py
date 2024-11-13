counter = 0
passed = 0
gradeList = []

for x in range(5):
    grade = int(input("Enter your grade: "))

    if grade < 40 or grade > 100:
        print("Invalid input. Number must be between 40 and 100")
        break
    else:
        gradeList.append(grade)
    
    if grade >= 75:
        passed += 1
        counter += 1
    else:
        counter += 1
    
if counter == 5:
    print()
    sumNums = sum(gradeList)
    averageGrade = sumNums / 5
    averageGrade = round(averageGrade, 2)
        
    passPercent = (passed / len(gradeList)) * 100
    passPercent = round(passPercent, 2)

    print("Grades inputted: " + str(gradeList))
    print("Average grade: " + str(averageGrade))
    print("Number of people who passed: " + str(passed))
    print("Percentage of people who passed: " + str(passPercent) + "%")