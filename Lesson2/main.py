age = int(input("age >>>"))
hour = int(input("what's an hour >>>"))
have_id = bool(int(input("do you have id card (1 - yes, 0 no) >>>")))

condition = (age >= 18 and have_id) and hour < 21

if (condition):
    print("You can buy alcohol")
else:
    print("You are too young")