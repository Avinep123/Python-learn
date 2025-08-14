age=int(input("Provide age : "))

if age<13:
    print("Child")
elif age<20:
    print("Teen")
elif age<60:
    print("Adult")
else:
    print("Senior")