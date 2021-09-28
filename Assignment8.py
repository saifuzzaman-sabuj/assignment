number=int(input("Enter tne number: "))
lucky_number=7
while True:
    if lucky_number==number:
        print("You won")
        break
    else:
        ans=input("Do you want to play again? press Yes or No: ")
        if ans=="no":
            print("Thank you for playing.")
            break
        else:
            number = int(input("Enter tne number: "))