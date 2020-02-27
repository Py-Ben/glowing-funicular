var1 = 1
while var1 == 1:
    print("\n\n\n\t\tWelcome to Ben's Calculator\n")
    do_you = input("\nWanna do some math? yes/no:") 
    if do_you == "no":
        break
    math_type = input("What would you like to do? add, subtract, multiply, or divide?")
    a = input("First number?")
    b = input("Second number?")

    if math_type == "add":
        answer = int(a) + int(b)
        print(f"{a}+{b}={answer}")   

    if math_type == "subtract":
        answer = int(a) - int(b)
        print(f"{a}-{b}={answer}") 

    if math_type == "multiply":
        answer = int(a) * int(b)
        print(f"{a}*{b}={answer}")  

    if math_type == "divide":
        answer = int(a) / int(b)
        print(f"{a}/{b}={answer}")
