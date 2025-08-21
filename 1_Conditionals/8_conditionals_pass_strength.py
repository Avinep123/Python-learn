password="Test@123456789"

if len(password) < 6:
    strength="Weak"
elif len(password)<=10:
    strength="Strong"
else:
    strength="Excellent"

print("Password strength is :", strength)
