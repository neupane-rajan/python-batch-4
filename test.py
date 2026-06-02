# driving license eligibility
# take age from the user.
# if age is 18 or above
# check if the user has passed the    driving test:
# display where the liscense can be issued or not.

age = int(input("enter your age: "))

if age >= 18:
    test_pass = input("did you passed your test?(y/n): ")
    if test_pass == "y":
        print("you are eligible for liscense!!")
    else:
        print("please give a test again")
else:
    print("you are too young for license!!")
