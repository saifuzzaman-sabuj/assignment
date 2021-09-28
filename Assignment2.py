
user_Enter=input("Enter the input: ")
num1=int(input("Emter the number: "))
num2=int(input("Emter the number: "))

if user_Enter=="Additation":
    result= num1+num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif user_Enter=="Subtraction":
    result= num1-num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif user_Enter=="Division":
    result= num1/num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif user_Enter=="Multiplication":
    result= num1*num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif user_Enter=="Average":
    num3 = int(input("Emter the number: "))
    num4 = int(input("Emter the number: "))
    result= (num1+num2+num3+num4)/2
    print(result)
    if result<0:
        print("NEGATIVE")