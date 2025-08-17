weather=input("Enter weather").lower()

if weather=="sunny":
    activity="Go for a walk"
elif weather=="rainy":
    activity="Read a book"
elif weather=="snowy":
    activity="Build a snowman"
else:
    activity="Enjoy your Day"

print(activity)