
days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5
}
day = input("Enter a day of the week:").strip().title()

if day in days.keys():
    print(f"{day} is day {days[day]}")
else:
    print("Please enter a valid day")
    

