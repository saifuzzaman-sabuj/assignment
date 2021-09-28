number=int(input("Enter tne number: "))
lucky_number=7
counter=1
while counter<=5:

    if lucky_number==number:
        print("Good guess!")

    else:
        print("Try again!")
    number = int(input("Enter tne number: "))
    counter=counter+1
print("Game over!")
