score=int(input("Enter your score"))

if (score > 100 or score < 0):
    print("Invalid grade must be between 0 to 100")
    exit()

if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="E"

print("Grade=",grade)