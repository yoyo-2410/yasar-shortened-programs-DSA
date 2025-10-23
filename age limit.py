from datetime import datetime

dob = input("Enter DOB (YYYY-MM-DD): ")
try:
    d = datetime.strptime(dob, '%Y-%m-%d')
    t = datetime.today()
    age = t.year - d.year - ((t.month, t.day) < (d.month, d.day))
    print("Age:", age)
    if age < 18: print("Underage, minimum age is 18.")
    elif age < 60: print("Within working age limit.")
    else: print("At or above retirement age.")
except:
    print("Invalid date format.")
