age = input("How old are you? ")
if age >= 18:
    print("You can vote because you are " + age + " years old")
else:
    wait_years = 18 - age
    print("You will need to wait" + wait_years + "years to vote")