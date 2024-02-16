current_users = ["marcel","mark","rita","ambrose","mary"]
new_users = ["marcel","mark","tosa","yaw","abena"]
for new_user in new_users:
    print(new_users)
if new_user in current_users :
    print(f"{new_users.title()} has been used already. Please enter a new user name")
else :
    print("Username is available")

# QUESTION 2
for num in range (1,101):
    if num % 3 == 0 and num % 5 == 0 :
        print("FizzBuzz")
    elif num % 3 == 0 :
        print("Fizz")
    elif num % 5 == 0 :
        print("Buzz")
    else:
        print(num)