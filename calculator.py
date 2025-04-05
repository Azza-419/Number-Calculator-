print("Welcome to the Calculator! Choose a number below to perform:")

while True:  
    values = ["1.Multiplication", "2.Division", "3.Subtraction", "4.Addition", "5.Quit"]
    for item in values:
        print(item)

    answer = int(input("What do you choose?:  "))

    # Condition to quit
    if answer == 5:
        print("Goodbye!")
        break  

     #operation
    if answer == 1:
        print(f"What would you like to Multiply?")
    elif answer == 2:
        print(f"What would you like to Divide?")
    elif answer == 3:
        print(f"What would you like to Subtract?")
    elif answer == 4:
        print(f"What would you like to Add?")

    # Input for the two numbers
    digit_1 = int(input("First number: "))
    digit_2 = int(input("Second number: "))

    # Perform the operation
    if answer == 1:
        outcome = digit_1 * digit_2
        print(f"Answer is: {outcome}")
    elif answer == 2:
        outcome = digit_1 / digit_2
        print(f"Answer is: {outcome}")
    elif answer == 3:
        outcome = digit_1 - digit_2
        print(f"Answer is: {outcome}")
    elif answer == 4:
        outcome = digit_1 + digit_2
        print(f"Answer is: {outcome}")
